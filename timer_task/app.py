from rocketry import Rocketry
from rocketry.args import Arg

app = Rocketry()

# Config of Timer Task
timer_params={
    'device':'', # device name
    'host':'', # cloud host which receives ip info
    'gp':'', #  yes or no to refresh Github Pages

}


@app.task('daily')
def refresh_github_pages():
    if timer_params['gp'] == 'yes':
        from job_gp.app import do_job
        do_job()


@app.task('every 10 minutes')
def send_info():
    from data_send.app import do_send
    do_send(timer_params['host'],timer_params['device'])


if __name__ == '__main__':
    app.run()
