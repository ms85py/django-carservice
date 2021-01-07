# django-carservice

The second Django project I've done, a Ticket-system for a Car-Service.

On the main page, you can request a ticket to either get your oil changed, tires inflated or to get a diagnostic test done on your car.

When getting your ticket you'll see your ticket number and an estimated wait time, which is calculated as follows:

Each oil change takes 2 minutes, getting your tires inflated takes 5 and a full diagnostics test takes 30 minutes.

People getting their oil changed get served first, if there's no oil change left, the tires are next. Last is diagnostics tests.

On /processing the mechanics can see how much tickets are in each line. There's also a button 'Process Next', which will show the mechanic which ticket is next / currently in processing.

**Libraries/Modules used:** None.
