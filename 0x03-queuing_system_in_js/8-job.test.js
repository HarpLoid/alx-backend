const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');
const assert = require('assert');

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    assert.throws(() => {
      createPushNotificationsJobs('not an array', queue);
    }, /Jobs is not an array/);
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Message 1' },
      { phoneNumber: '0987654321', message: 'Message 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    const createdJobs = queue.testMode.jobs['push_notification_code_3'];
    assert.strictEqual(createdJobs.length, 2);
  });

  it('should log job creation', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Message 1' },
      { phoneNumber: '0987654321', message: 'Message 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    const createdJobs = queue.testMode.jobs['push_notification_code_3'];
    createdJobs.forEach(job => {
      assert.ok(job.log.calledWithMatch(/Notification job created:/));
    });
  });
});
