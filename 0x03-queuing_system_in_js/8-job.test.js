import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const kue = require('kue');

const queue = kue.createQueue();

const listJobs = [
  {
    phoneNumber: '0002',
    message: 'Message_2',
  },
  {
    phoneNumber: '0003',
    message: 'Message_3',
  },
  {
    phoneNumber: '0004',
    message: 'Message_4',
  },
  {
    phoneNumber: '0005',
    message: 'Message_5',
  },
];

after(() => {
  queue.testMode.exit();
});

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  // it('should return a push notification job', () => {
  //   const notificationObj = createPushNotificationsJobs(listJobs, queue);
  //   expect(notificationObj).to.be.an('object');
  // });

  it('valid Data', () => {
    createPushNotificationsJobs(listJobs, queue);
    expect(queue.testMode.jobs.length).to.equal(4);

    createPushNotificationsJobs(listJobs, queue);
    expect(queue.testMode.jobs.length).to.equal(8);
  });

  it('invalid Data', () => {
    expect(() => createPushNotificationsJobs('', queue)).to.throw(Error);
    expect(() => createPushNotificationsJobs(123, queue)).to.throw(Error);
    expect(() => createPushNotificationsJobs({ id: 120 }, queue)).to.throw(Error);
    expect(() => createPushNotificationsJobs(NaN, queue)).to.throw(Error);
  });

  afterEach(() => {
    queue.testMode.clear();
  });
});
