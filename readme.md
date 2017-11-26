# CTA Transit Tracker
## A project to make an LED sign with Python
[example of objective](https://www.raspberrypi.org/app/uploads/2017/07/Wall-Big_01-500x291.jpg)
### Objective:
Build a "transit tracker" app that runs on Raspberry Pi and outputs to an LED matrix to display:
1. Next incoming train times for a specific station.
2. Current weather conditions.
3. Upcoming Google Calendar appointments.

### Tools needed:
- [] CTA Train Tracker API
- [] Some weather service API (DarkSky, NWS, Open Weather Map, TBD)
- [] Google Calendar OAuth

### Production Notes
- on line 67 we use `r_south`, there is a chance that based on location, you will only get southbound routes.
- this could be remedied by duplicating the process used for `r_south` with already-defined `r_north`, but is not Pythonic due to repetition.
- it is also possible that, because I am working on this from DC- outside Chicago, that I am already significantly south of the 22's ending terminus and therefore only get northbound results.
1. establish wtf is going on with the _bus direction_
2. figure out how to print **BOTH directions** for nearest stops (the stops will have different IDs)
3. what are we going to do if a stop has multiple routes?
