
class timesheet{
    constructor(qrCode,startDate, startTime, endDate,endTime){
        this.qrCode = qrCode;
        this.startDate = startDate;
        this.startTime = startTime;
        this.endDate = endDate;
        this.endTime = endTime;
    }

    calcDifference(){
        let start = new Date(this.startDate + " " + this.startTime);
        let end = new Date(this.endDate + " " + this.endTime);
        let difference = end - start;
        let hours = Math.floor(difference / 1000 / 60 / 60);
        difference -= hours * 1000 * 60 * 60;
        let minutes = Math.floor(difference / 1000 / 60);
        difference -= minutes * 1000 * 60;
        let seconds = Math.floor(difference / 1000);
        difference -= seconds * 1000;
        return hours + " hours " + minutes + " minutes " + seconds + " seconds";
    }

    getCurrentDateTime(){
        let today = new Date();
        let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        return date + " " + time;
    }
}

