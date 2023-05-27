const kue = require('kue');

const queue = kue.createQueue();

const data = {
    phoneNumber: '99999',
    message: 'MESSAGE',
}
// queue.create('push_notification_code', data).save((err, job) => {
//     if (err) return console.log(err);
//     console.log(`Notification job created: ${job.id}`);
//     });
    
const job = queue.create('push_notification_code', data).save((err) => {
    if(!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));

// job.on('progress', (progress) => console.log('Notification job progress:', progress));
// job.on('error', (err) => console.log('Notification job error:', err));
// job.on('paused', () => console.log('Notification job paused'));
// job.on('active', () => console.log('Notification job active'));
// job.on('timeout', () => console.log('Notification job timed out'));
// job.on('progress', (progress) => console.log('Notification job progress:', progress));
