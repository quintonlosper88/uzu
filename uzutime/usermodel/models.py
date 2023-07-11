from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import qrcode
from datetime import datetime
import pytz
# Create your models here.
class UserModel(models.Model):
    firstName = models.CharField(max_length=100);
    lastName = models.CharField(max_length=100);
    email = models.EmailField(max_length=100);
    employeeID = models.CharField(max_length=20);
    position = models.CharField(max_length=50);
    address=models.CharField(max_length=200);
    phone_number = PhoneNumberField(blank=False,region="ZA")
    contractHours = models.DecimalField(decimal_places=2,max_digits=100)
    profileImage = models.ImageField(upload_to='profiles/')
    working_status = models.BooleanField(default=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)


    def __str__(self):
        return self.firstName + ' ' + self.lastName


    def save(self, *args, **kwargs):
        # Generate QR code data based on first name and employee ID
        qr_data = f"{self.employeeID}"

        # Create a QR code instance and add the data
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Generate the QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to the user's qr_code field
        # Make sure to install 'Pillow' library for image handling: pip install pillow
        from io import BytesIO
        from django.core.files import File
        import os

        # Prepare the file name and path
        filename = f"{self.employeeID}.png"
        filepath = os.path.join('qr_codes', filename)

        # Create a BytesIO stream to temporarily hold the image data
        temp_image = BytesIO()
        qr_image.save(temp_image, format='PNG')
        temp_image.seek(0)

        # Set the user's qr_code field with the saved image file
        self.qr_code.save(filepath, File(temp_image), save=False)

        super().save(*args, **kwargs)

class Timesheet(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    enter_time = models.DateTimeField()
    leave_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        print(type(self.enter_time))
        print(type(self.leave_time))
        if self.enter_time and self.leave_time:
            if isinstance(self.leave_time, str):
                self.leave_time = datetime.strptime(self.leave_time, '%Y-%m-%d %H:%M:%S')
                print(type(self.leave_time))
                self.leave_time = pytz.timezone('Africa/Accra').localize(self.leave_time)
                print(type(self.leave_time))
            self.duration = self.leave_time - self.enter_time

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.enter_time}"
