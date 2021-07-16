# Personal Covid Map

## Testing
While testing can use this temporary token to access Mapbox:
`export MapboxAccessToken=pk.eyJ1IjoiamFjay1zY290dCIsImEiOiJja3I2MTd1eGUwbG5kMnhyMmJoNXY1MnFzIn0.6jo22QLMPFR_7f-11tuWtQ`


## Troubleshooting
If you exceed the number of file system watches i.e.  
`Error from chokidar (/usr/src/app/personal_covid_map/demo-app/src/data): Error: ENOSPC: System limit for number of file watchers reached, watch '/usr/src/app/personal_covid_map/demo-app/src/data/sample-trip-data.js'`  
You can increase the number by using to follwing commands on the **host** computer (this /proc/ is shared with the docker container as read only):     
`echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf`
`sudo sysctl -p`