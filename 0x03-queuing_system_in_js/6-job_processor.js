const kue = require('kue');
const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// queue.process('send notification', (job, done) => {
//     const phoneNumber = job.data.phoneNumber;
//     const message = job.data.message;
//     sendNotification(phoneNumber, message);
//     done();
//     });

queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});
