# [hold-my-spot](https://hold-my-spot.herokuapp.com/) - https://hold-my-spot.herokuapp.com/
CRUD Reservation system
---

### Goal
**Short term**
- Create an event reservation system to facilitate event capacity management and access control to events

**Long term**
- Create a SaaS application for event management to handle recurring event scheduling, subscription payments, sms and email notifications

---

### Milestones:
- [x] Landing Page
- [x] Login screen
- [x] Signup screen
- [ ] Dashboard showing upcoming Events(For admins, it allows management of the event and adding walk-ins)
- [ ] Event sign up screen


---
### SQL Tables needed:
- Users table: Stores users and passwords along with contact information
- Events table: Stores the event data
- event_admin table: Stores Admins to the events
- event_attendee table: Stores the attendees of the events
- leads table: Stores walkin users email address for creating future accounts(stretch)

#### Entity Relationship Diagram:
![Entity_relationship](er-diagram.png)

---
### User stories

#### Event planner:
- Event Planner Joseph, has a new event on March 13 2022 at a specific place
- Joseph signs up on "hold-my-spot"
- Joseph creates an event
- Joseph publishes the event and gets a custom link to the event that can be published or emailed to his audience

#### Event attendee:
- Event Attendee Mike, received a link to sign up for the event
- Mike goes to the link and creates an account
- Once Mike is logged in, he can register for the event and receive a confirmation email (extension: QR code)

#### Event planner on the day of the event:
- Joseph opens up "hold-my-spot"
- Joseph can see the names, and emails of the attendees that signed up for the class
- Joseph can mark someone as absent, which frees up a space on the class
- Joseph can register users on their behalf in case of walk-ins

#### Event planner after the event:
- Joseph can download a list of attendees for future contact
- Joseph can create a new event based on the same characteristics of the previous one

#### Attendees after the event: (Stretch)
- Mike can now create his own events as well
- Mike can re-use his account for future events managed by "hold-my-spot"

- John (walk-in) receives an email with instructions to create an account in the future if needed