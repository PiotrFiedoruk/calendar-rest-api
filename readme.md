## About repository
Backend Django Rest API I was asked to create for a job interview in one of the software houses


##Background

Create a simple RESTful API for managing calendar events and
conference room availability. The application would be deployed in a multitenant model,
where multiple companies would store their data on a central server.
For simplicity, please assume that the user model contains an additional UUID field -
company_id. Users sharing the same company_id will belong to the same company.

##Business requirements

Each user should have his/her default timezone. All endpoints should be timezone-aware and
return results in the timezone of the currently logged in user.
There’s no need to implement the user management API - we can assume that for the
purpose of this task it is done via Django Administration Panel or through the Django Shell.
The business domain of the application should consists of two core resources:

Conference room (location):

1. Manager (a user on the platform)
2. Name
3. Address

Calendar event (meeting):

1. Owner (a user on the platform)
2. Event name
3. Meeting agenda
4. Start
5. End
6. Participant list (platform users, input provided by their e-mail addresses)
7. Location (optional)

####On top of the basic create/retrieve operations, the API should also allow clients to:
- retrieve events happening on a specific day (?day=2020-12-12)

- retrieve events happening in a specific conference room (?location_id=6fb94459)
- search events by name / agenda (?query=sprint+retrospective)
- see the serialized nested representation of conference rooms when listing events
To keep things simple, there is no need to implement update and delete operations.
There are three additional requirements that should be met:
- meeting owner should always be the person who created the meeting
- meetings shouldn’t be longer than 8 hours
- events shouldn’t be visible to people who are not participating, unless they are the
manager of the corresponding conference room