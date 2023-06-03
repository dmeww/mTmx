from rocketry import Rocketry
from rocketry.args import Arg
from data_send.app import do_send
from job_gp.app import do_refresh
app = Rocketry()

# Config of Timer Task
timer_params={
    'device':'', # device name
    'host':'', # cloud host which receives ip info
    'gp':'', #  yes or no to refresh Github Pages

}


@app.task('every 24 hour')
def refresh_github_pages():
    if timer_params['gp'] == 'yes':
        do_refresh()



@app.task('every 1 minute')
def send_info():
    print('sending ip')
    do_send(timer_params['host'],timer_params['device'])


if __name__ == '__main__':
    app.run()
