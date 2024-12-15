Liveheats GraphQL API Reference
Liveheats uses a GraphQL API to display data on the public website (https://liveheats.com). All screens that you see when navigating through organisations and events in the Liveheats website fetch their data using the Liveheats API, so anything that you can see on the website, you can get through this API to display where and how you need.

GraphQL is a very powerful query language for APIs that allows developers to predictably extract the exact data they need by traversing the schema available. It does, however, require a bit of knowledge on how it works in order to get properly started, so if you are unfamiliar with GraphQL and it's main concepts, we suggest reading about it in https://graphql.org/learn/

The rest of this guide assumes familiarity with GraphQL Queries and their Variables and Types. It is also beneficial to get acquainted with Liveheats' data structure

Contact
API Support

community@liveheats.com

Terms of Service
https://liveheats.com/terms_and_conditions

API Endpoints
# Staging:
https://staging.liveheats.com/api/graphql
# Production:
https://liveheats.com/api/graphql
Headers
Authorization: Bearer <YOUR_TOKEN_HERE>
Queries
athlete
Description
Get an athlete by it's id

Response
Returns an Athlete

Arguments
Name	Description
id - ID!	
Example
Query
query athlete($id: ID!) {
  athlete(id: $id) {
    appearances {
      ...CompetitorFragment
    }
    createdAt
    dob
    entries {
      ...AthleteEntryFragment
    }
    entriesWithPendingPayments {
      ...EntryFragment
    }
    eventDivisions {
      ...EventDivisionFragment
    }
    id
    image
    memberships {
      ...AthleteMembershipFragment
    }
    name
    nationality
    physicalTags {
      ...PhysicalTagFragment
    }
    properties
    ranks {
      ...EventDivisionRankFragment
    }
    unfinishedEvents {
      ...EventFragment
    }
    updatedAt
    users {
      ...UserFragment
    }
  }
}
Variables
{"id": 4}
Response
{
  "data": {
    "athlete": {
      "appearances": [Competitor],
      "createdAt": ISO8601Date,
      "dob": ISO8601Date,
      "entries": [AthleteEntry],
      "entriesWithPendingPayments": [Entry],
      "eventDivisions": [EventDivision],
      "id": "4",
      "image": "xyz789",
      "memberships": [AthleteMembership],
      "name": "abc123",
      "nationality": "xyz789",
      "physicalTags": [PhysicalTag],
      "properties": {},
      "ranks": [EventDivisionRank],
      "unfinishedEvents": [Event],
      "updatedAt": ISO8601Date,
      "users": [User]
    }
  }
}
Queries
contest
Description
Get a contest by it's id

Response
Returns a Contest

Arguments
Name	Description
id - ID!	
Example
Query
query contest($id: ID!) {
  contest(id: $id) {
    config {
      ...ContestConfigFragment
    }
    id
    name
    parent {
      ...ContestFragment
    }
    result {
      ... on PointsPerPlaceResult {
        ...PointsPerPlaceResultFragment
      }
    }
    savedConfig {
      ...ContestConfigFragment
    }
    type
  }
}
Variables
{"id": "4"}
Response
{
  "data": {
    "contest": {
      "config": ContestConfig,
      "id": "4",
      "name": "xyz789",
      "parent": Contest,
      "result": [PointsPerPlaceResult],
      "savedConfig": ContestConfig,
      "type": "xyz789"
    }
  }
}
Queries
currentUserRegion
Description
Get region from user IP location

Response
Returns a Region!

Example
Query
query currentUserRegion {
  currentUserRegion {
    currency
    name
  }
}
Response
{
  "data": {
    "currentUserRegion": {
      "currency": "xyz789",
      "name": "xyz789"
    }
  }
}
Queries
event
Description
Get an event by it's id

Response
Returns an Event

Arguments
Name	Description
id - ID!	
Example
Query
query event($id: ID!) {
  event(id: $id) {
    activeEntriesUsers {
      ...UserFragment
    }
    captureFields {
      ...PropertyFragment
    }
    config {
      ...EventConfigFragment
    }
    currentHeats {
      ...HeatFragment
    }
    currentScheduleIndex
    date
    daysWindow
    eventDivisions {
      ...EventDivisionFragment
    }
    fullSchedule {
      ...ScheduleFragment
    }
    hideEntries
    hideFinals
    hideScheduledTime
    id
    location {
      ...LocationFragment
    }
    name
    organisation {
      ...OrganisationFragment
    }
    organisationId
    paymentOptions {
      ...PaymentOptionsFragment
    }
    priorityEnabled
    registrationOptions {
      ...RegistrationOptionsFragment
    }
    seedFromSeriesId
    sentEmails {
      ...EmailFragment
    }
    series {
      ...SeriesFragment
    }
    status
    teamLeaderboard {
      ...EventTeamLeaderboardFragment
    }
    teams {
      ...TeamFragment
    }
    youtubeVideoId
  }
}
Variables
{"id": "4"}
Response
{
  "data": {
    "event": {
      "activeEntriesUsers": [User],
      "captureFields": [Property],
      "config": EventConfig,
      "currentHeats": [Heat],
      "currentScheduleIndex": 987,
      "date": ISO8601DateTime,
      "daysWindow": 123,
      "eventDivisions": [EventDivision],
      "fullSchedule": Schedule,
      "hideEntries": true,
      "hideFinals": true,
      "hideScheduledTime": false,
      "id": "4",
      "location": Location,
      "name": "xyz789",
      "organisation": Organisation,
      "organisationId": 4,
      "paymentOptions": PaymentOptions,
      "priorityEnabled": true,
      "registrationOptions": RegistrationOptions,
      "seedFromSeriesId": 4,
      "sentEmails": [Email],
      "series": [Series],
      "status": "scheduled",
      "teamLeaderboard": EventTeamLeaderboard,
      "teams": [Team],
      "youtubeVideoId": "xyz789"
    }
  }
}
Queries
eventCompetitors
Description
Find athletes in heats for an event

Response
Returns [CompetitorResult!]!

Arguments
Name	Description
eventId - ID!	
query - String!	The query string to search for competitors. An empty string will return empty results as opposed to every single competitor in the event
Example
Query
query eventCompetitors(
  $eventId: ID!,
  $query: String!
) {
  eventCompetitors(
    eventId: $eventId,
    query: $query
  ) {
    ... on Competitor {
      ...CompetitorFragment
    }
    ... on Entry {
      ...EntryFragment
    }
  }
}
Variables
{
  "eventId": "4",
  "query": "xyz789"
}
Response
{"data": {"eventCompetitors": [Competitor]}}
Queries
eventDivision
Description
Get an event division by it's id

Response
Returns an EventDivision

Arguments
Name	Description
id - ID!	
Example
Query
query eventDivision($id: ID!) {
  eventDivision(id: $id) {
    contestId
    defaultEventDurationMinutes
    division {
      ...DivisionFragment
    }
    divisionToSeasons {
      ...DivisionToSeasonsFragment
    }
    entries {
      ...EntryFragment
    }
    entryCount
    entryLimit {
      ...EntryLimitFragment
    }
    event {
      ...EventFragment
    }
    eventDivision {
      ...EventDivisionFragment
    }
    eventDivisionId
    eventDivisionPointAllocations {
      ...EventDivisionPointAllocationsFragment
    }
    eventDivisions {
      ...EventDivisionFragment
    }
    formatDefinition {
      ...FormatDefinitionFragment
    }
    heatConfig {
      ...HeatConfigFragment
    }
    heatDurationMinutes
    heats {
      ...HeatFragment
    }
    id
    leaderboards {
      ...LeaderboardFragment
    }
    order
    previewDraw {
      ...PreviewDrawFragment
    }
    properties
    ranking {
      ...EventDivisionRankFragment
    }
    seededRounds {
      ...SeededRoundFragment
    }
    status
    teamLeaderboard {
      ...EventDivisionTeamLeaderboardFragment
    }
    template {
      ...TemplateFragment
    }
  }
}
Variables
{"id": "4"}
Response
{
  "data": {
    "eventDivision": {
      "contestId": 4,
      "defaultEventDurationMinutes": 987,
      "division": Division,
      "divisionToSeasons": [DivisionToSeasons],
      "entries": [Entry],
      "entryCount": 123,
      "entryLimit": EntryLimit,
      "event": Event,
      "eventDivision": EventDivision,
      "eventDivisionId": "4",
      "eventDivisionPointAllocations": [
        EventDivisionPointAllocations
      ],
      "eventDivisions": [EventDivision],
      "formatDefinition": FormatDefinition,
      "heatConfig": HeatConfig,
      "heatDurationMinutes": 123,
      "heats": [Heat],
      "id": 4,
      "leaderboards": [Leaderboard],
      "order": 123,
      "previewDraw": PreviewDraw,
      "properties": {},
      "ranking": [EventDivisionRank],
      "seededRounds": [SeededRound],
      "status": "registration_open",
      "teamLeaderboard": EventDivisionTeamLeaderboard,
      "template": Template
    }
  }
}
Queries
eventsByName
Description
get a list of events that contain the search string name

Response
Returns [Event!]

Arguments
Name	Description
search - String!	
limit - Int	
eventLive - Boolean	
Example
Query
query eventsByName(
  $search: String!,
  $limit: Int,
  $eventLive: Boolean
) {
  eventsByName(
    search: $search,
    limit: $limit,
    eventLive: $eventLive
  ) {
    activeEntriesUsers {
      ...UserFragment
    }
    captureFields {
      ...PropertyFragment
    }
    config {
      ...EventConfigFragment
    }
    currentHeats {
      ...HeatFragment
    }
    currentScheduleIndex
    date
    daysWindow
    eventDivisions {
      ...EventDivisionFragment
    }
    fullSchedule {
      ...ScheduleFragment
    }
    hideEntries
    hideFinals
    hideScheduledTime
    id
    location {
      ...LocationFragment
    }
    name
    organisation {
      ...OrganisationFragment
    }
    organisationId
    paymentOptions {
      ...PaymentOptionsFragment
    }
    priorityEnabled
    registrationOptions {
      ...RegistrationOptionsFragment
    }
    seedFromSeriesId
    sentEmails {
      ...EmailFragment
    }
    series {
      ...SeriesFragment
    }
    status
    teamLeaderboard {
      ...EventTeamLeaderboardFragment
    }
    teams {
      ...TeamFragment
    }
    youtubeVideoId
  }
}
Variables
{
  "search": "xyz789",
  "limit": 123,
  "eventLive": false
}
Response
{
  "data": {
    "eventsByName": [
      {
        "activeEntriesUsers": [User],
        "captureFields": [Property],
        "config": EventConfig,
        "currentHeats": [Heat],
        "currentScheduleIndex": 123,
        "date": ISO8601DateTime,
        "daysWindow": 123,
        "eventDivisions": [EventDivision],
        "fullSchedule": Schedule,
        "hideEntries": true,
        "hideFinals": false,
        "hideScheduledTime": false,
        "id": "4",
        "location": Location,
        "name": "abc123",
        "organisation": Organisation,
        "organisationId": 4,
        "paymentOptions": PaymentOptions,
        "priorityEnabled": true,
        "registrationOptions": RegistrationOptions,
        "seedFromSeriesId": 4,
        "sentEmails": [Email],
        "series": [Series],
        "status": "scheduled",
        "teamLeaderboard": EventTeamLeaderboard,
        "teams": [Team],
        "youtubeVideoId": "abc123"
      }
    ]
  }
}
Queries
featuredEvents
Description
get the list of featured events

Response
Returns [Event!]!

Example
Query
query featuredEvents {
  featuredEvents {
    activeEntriesUsers {
      ...UserFragment
    }
    captureFields {
      ...PropertyFragment
    }
    config {
      ...EventConfigFragment
    }
    currentHeats {
      ...HeatFragment
    }
    currentScheduleIndex
    date
    daysWindow
    eventDivisions {
      ...EventDivisionFragment
    }
    fullSchedule {
      ...ScheduleFragment
    }
    hideEntries
    hideFinals
    hideScheduledTime
    id
    location {
      ...LocationFragment
    }
    name
    organisation {
      ...OrganisationFragment
    }
    organisationId
    paymentOptions {
      ...PaymentOptionsFragment
    }
    priorityEnabled
    registrationOptions {
      ...RegistrationOptionsFragment
    }
    seedFromSeriesId
    sentEmails {
      ...EmailFragment
    }
    series {
      ...SeriesFragment
    }
    status
    teamLeaderboard {
      ...EventTeamLeaderboardFragment
    }
    teams {
      ...TeamFragment
    }
    youtubeVideoId
  }
}
Response
{
  "data": {
    "featuredEvents": [
      {
        "activeEntriesUsers": [User],
        "captureFields": [Property],
        "config": EventConfig,
        "currentHeats": [Heat],
        "currentScheduleIndex": 987,
        "date": ISO8601DateTime,
        "daysWindow": 987,
        "eventDivisions": [EventDivision],
        "fullSchedule": Schedule,
        "hideEntries": true,
        "hideFinals": true,
        "hideScheduledTime": true,
        "id": "4",
        "location": Location,
        "name": "xyz789",
        "organisation": Organisation,
        "organisationId": "4",
        "paymentOptions": PaymentOptions,
        "priorityEnabled": true,
        "registrationOptions": RegistrationOptions,
        "seedFromSeriesId": "4",
        "sentEmails": [Email],
        "series": [Series],
        "status": "scheduled",
        "teamLeaderboard": EventTeamLeaderboard,
        "teams": [Team],
        "youtubeVideoId": "xyz789"
      }
    ]
  }
}
Queries
federationAthletes
Response
Returns an OrganisationAthletes!

Arguments
Name	Description
id - ID!	
search - String	
athleteId - ID	
page - Int!	
per - Int!	
Example
Query
query federationAthletes(
  $id: ID!,
  $search: String,
  $athleteId: ID,
  $page: Int!,
  $per: Int!
) {
  federationAthletes(
    id: $id,
    search: $search,
    athleteId: $athleteId,
    page: $page,
    per: $per
  ) {
    athletes {
      ...AthleteFragment
    }
    totalCount
  }
}
Variables
{
  "id": 4,
  "search": "xyz789",
  "athleteId": 4,
  "page": 123,
  "per": 987
}
Response
{
  "data": {
    "federationAthletes": {
      "athletes": [Athlete],
      "totalCount": 123
    }
  }
}
Queries
federationTeams
Description
Get a list of teams linked to federation

Response
Returns a FederationTeams!

Arguments
Name	Description
id - ID!	
search - String	
teamId - ID	
page - Int!	
per - Int!	
Example
Query
query federationTeams(
  $id: ID!,
  $search: String,
  $teamId: ID,
  $page: Int!,
  $per: Int!
) {
  federationTeams(
    id: $id,
    search: $search,
    teamId: $teamId,
    page: $page,
    per: $per
  ) {
    teams {
      ...TeamFragment
    }
    totalCount
  }
}
Variables
{
  "id": 4,
  "search": "abc123",
  "teamId": 4,
  "page": 987,
  "per": 123
}
Response
{
  "data": {
    "federationTeams": {
      "teams": [Team],
      "totalCount": 987
    }
  }
}
Queries
heat
Description
Get a heat by it's id

Response
Returns a Heat

Arguments
Name	Description
id - ID!	
Example
Query
query heat($id: ID!) {
  heat(id: $id) {
    competitors {
      ...CompetitorFragment
    }
    config {
      ...HeatConfigFragment
    }
    contestId
    endTime
    eventDivision {
      ...EventDivisionFragment
    }
    eventDivisionId
    group {
      ...HeatGroupFragment
    }
    heatDurationMinutes
    id
    podium
    position
    progressions {
      ...HeatProgressionFragment
    }
    result {
      ...HeatResultFragment
    }
    round
    roundPosition
    scheduledTime
    startTime
  }
}
Variables
{"id": "4"}
Response
{
  "data": {
    "heat": {
      "competitors": [Competitor],
      "config": HeatConfig,
      "contestId": 4,
      "endTime": ISO8601DateTime,
      "eventDivision": EventDivision,
      "eventDivisionId": "4",
      "group": HeatGroup,
      "heatDurationMinutes": 987,
      "id": 4,
      "podium": "abc123",
      "position": 123,
      "progressions": [HeatProgression],
      "result": [HeatResult],
      "round": "abc123",
      "roundPosition": 123,
      "scheduledTime": ISO8601DateTime,
      "startTime": ISO8601DateTime
    }
  }
}
Queries
organisation
Description
Get an organisation by it's id, only available for authenticated directors of the organisation

Response
Returns an Organisation

Arguments
Name	Description
id - ID!	
Example
Query
query organisation($id: ID!) {
  organisation(id: $id) {
    activePurchases {
      ...ActivePurchasesFragment
    }
    contactEmail
    customProperties {
      ...PropertyFragment
    }
    divisions {
      ...DivisionFragment
    }
    docusealEnabled
    events {
      ...EventFragment
    }
    facebook
    federatedOrganisationTerm
    federatedOrganisations {
      ...OrganisationFragment
    }
    federationPointAllocations {
      ...PointAllocationFragment
    }
    federationProperties {
      ...PropertyFragment
    }
    federationSeries {
      ...SeriesFragment
    }
    federationTeams {
      ...TeamFragment
    }
    federationTemplates {
      ...TemplateFragment
    }
    id
    instagram
    latestPayment {
      ...PaymentFragment
    }
    logo
    name
    payables {
      ... on Event {
        ...EventFragment
      }
      ... on Series {
        ...SeriesFragment
      }
    }
    paymentsEnabled
    paymentsReceived {
      ...PaymentsFragment
    }
    series {
      ...SeriesFragment
    }
    shortName
    sportType
    stripeAccountDetails {
      ...StripeAccountDetailsFragment
    }
    transactionFee
    useNfc
  }
}
Variables
{"id": 4}
Response
{
  "data": {
    "organisation": {
      "activePurchases": ActivePurchases,
      "contactEmail": "abc123",
      "customProperties": [Property],
      "divisions": [Division],
      "docusealEnabled": true,
      "events": [Event],
      "facebook": "abc123",
      "federatedOrganisationTerm": "xyz789",
      "federatedOrganisations": [Organisation],
      "federationPointAllocations": [PointAllocation],
      "federationProperties": [Property],
      "federationSeries": [Series],
      "federationTeams": [Team],
      "federationTemplates": [Template],
      "id": "4",
      "instagram": "xyz789",
      "latestPayment": Payment,
      "logo": "abc123",
      "name": "xyz789",
      "payables": [Event],
      "paymentsEnabled": false,
      "paymentsReceived": Payments,
      "series": [Series],
      "shortName": "abc123",
      "sportType": "abc123",
      "stripeAccountDetails": StripeAccountDetails,
      "transactionFee": 987.65,
      "useNfc": false
    }
  }
}
Queries
organisationAthletes
Description
Get a list of athletes linked to organisation (including descendants for federations)

Response
Returns an OrganisationAthletes!

Arguments
Name	Description
id - ID!	
search - String	
athleteId - ID	
page - Int!	
per - Int!	
Example
Query
query organisationAthletes(
  $id: ID!,
  $search: String,
  $athleteId: ID,
  $page: Int!,
  $per: Int!
) {
  organisationAthletes(
    id: $id,
    search: $search,
    athleteId: $athleteId,
    page: $page,
    per: $per
  ) {
    athletes {
      ...AthleteFragment
    }
    totalCount
  }
}
Variables
{
  "id": 4,
  "search": "xyz789",
  "athleteId": "4",
  "page": 123,
  "per": 987
}
Response
{
  "data": {
    "organisationAthletes": {
      "athletes": [Athlete],
      "totalCount": 123
    }
  }
}
Queries
organisationByShortName
Description
Get an organisation by it's short name

Response
Returns an Organisation

Arguments
Name	Description
shortName - String	
Example
Query
query organisationByShortName($shortName: String) {
  organisationByShortName(shortName: $shortName) {
    activePurchases {
      ...ActivePurchasesFragment
    }
    contactEmail
    customProperties {
      ...PropertyFragment
    }
    divisions {
      ...DivisionFragment
    }
    docusealEnabled
    events {
      ...EventFragment
    }
    facebook
    federatedOrganisationTerm
    federatedOrganisations {
      ...OrganisationFragment
    }
    federationPointAllocations {
      ...PointAllocationFragment
    }
    federationProperties {
      ...PropertyFragment
    }
    federationSeries {
      ...SeriesFragment
    }
    federationTeams {
      ...TeamFragment
    }
    federationTemplates {
      ...TemplateFragment
    }
    id
    instagram
    latestPayment {
      ...PaymentFragment
    }
    logo
    name
    payables {
      ... on Event {
        ...EventFragment
      }
      ... on Series {
        ...SeriesFragment
      }
    }
    paymentsEnabled
    paymentsReceived {
      ...PaymentsFragment
    }
    series {
      ...SeriesFragment
    }
    shortName
    sportType
    stripeAccountDetails {
      ...StripeAccountDetailsFragment
    }
    transactionFee
    useNfc
  }
}
Variables
{"shortName": "xyz789"}
Response
{
  "data": {
    "organisationByShortName": {
      "activePurchases": ActivePurchases,
      "contactEmail": "abc123",
      "customProperties": [Property],
      "divisions": [Division],
      "docusealEnabled": true,
      "events": [Event],
      "facebook": "abc123",
      "federatedOrganisationTerm": "abc123",
      "federatedOrganisations": [Organisation],
      "federationPointAllocations": [PointAllocation],
      "federationProperties": [Property],
      "federationSeries": [Series],
      "federationTeams": [Team],
      "federationTemplates": [Template],
      "id": 4,
      "instagram": "abc123",
      "latestPayment": Payment,
      "logo": "abc123",
      "name": "xyz789",
      "payables": [Event],
      "paymentsEnabled": false,
      "paymentsReceived": Payments,
      "series": [Series],
      "shortName": "abc123",
      "sportType": "abc123",
      "stripeAccountDetails": StripeAccountDetails,
      "transactionFee": 987.65,
      "useNfc": true
    }
  }
}
Queries
organisationUsers
Description
Get a list of judges and directors linked to organisation

Response
Returns [User!]

Arguments
Name	Description
id - ID!	
Example
Query
query organisationUsers($id: ID!) {
  organisationUsers(id: $id) {
    athletes {
      ...AthleteFragment
    }
    competitors {
      ...CompetitorFragment
    }
    email
    entries {
      ...EntryFragment
    }
    eventAthletes {
      ...AthleteFragment
    }
    eventEmails {
      ...EmailFragment
    }
    id
    image
    name
    pendingPayments {
      ...PaymentFragment
    }
    phone
    properties
    role
    unfinishedEvents {
      ...EventFragment
    }
  }
}
Variables
{"id": 4}
Response
{
  "data": {
    "organisationUsers": [
      {
        "athletes": [Athlete],
        "competitors": [Competitor],
        "email": "abc123",
        "entries": [Entry],
        "eventAthletes": [Athlete],
        "eventEmails": [Email],
        "id": "4",
        "image": "abc123",
        "name": "xyz789",
        "pendingPayments": [Payment],
        "phone": "xyz789",
        "properties": {},
        "role": "abc123",
        "unfinishedEvents": [Event]
      }
    ]
  }
}
Queries
organisationsByName
Description
get a list of organisations that contain the search string name or short name

Response
Returns [Organisation!]

Arguments
Name	Description
search - String!	
limit - Int	
Example
Query
query organisationsByName(
  $search: String!,
  $limit: Int
) {
  organisationsByName(
    search: $search,
    limit: $limit
  ) {
    activePurchases {
      ...ActivePurchasesFragment
    }
    contactEmail
    customProperties {
      ...PropertyFragment
    }
    divisions {
      ...DivisionFragment
    }
    docusealEnabled
    events {
      ...EventFragment
    }
    facebook
    federatedOrganisationTerm
    federatedOrganisations {
      ...OrganisationFragment
    }
    federationPointAllocations {
      ...PointAllocationFragment
    }
    federationProperties {
      ...PropertyFragment
    }
    federationSeries {
      ...SeriesFragment
    }
    federationTeams {
      ...TeamFragment
    }
    federationTemplates {
      ...TemplateFragment
    }
    id
    instagram
    latestPayment {
      ...PaymentFragment
    }
    logo
    name
    payables {
      ... on Event {
        ...EventFragment
      }
      ... on Series {
        ...SeriesFragment
      }
    }
    paymentsEnabled
    paymentsReceived {
      ...PaymentsFragment
    }
    series {
      ...SeriesFragment
    }
    shortName
    sportType
    stripeAccountDetails {
      ...StripeAccountDetailsFragment
    }
    transactionFee
    useNfc
  }
}
Variables
{"search": "xyz789", "limit": 987}
Response
{
  "data": {
    "organisationsByName": [
      {
        "activePurchases": ActivePurchases,
        "contactEmail": "abc123",
        "customProperties": [Property],
        "divisions": [Division],
        "docusealEnabled": true,
        "events": [Event],
        "facebook": "abc123",
        "federatedOrganisationTerm": "abc123",
        "federatedOrganisations": [Organisation],
        "federationPointAllocations": [PointAllocation],
        "federationProperties": [Property],
        "federationSeries": [Series],
        "federationTeams": [Team],
        "federationTemplates": [Template],
        "id": 4,
        "instagram": "xyz789",
        "latestPayment": Payment,
        "logo": "abc123",
        "name": "abc123",
        "payables": [Event],
        "paymentsEnabled": false,
        "paymentsReceived": Payments,
        "series": [Series],
        "shortName": "xyz789",
        "sportType": "xyz789",
        "stripeAccountDetails": StripeAccountDetails,
        "transactionFee": 123.45,
        "useNfc": false
      }
    ]
  }
}
Queries
payment
Description
Get a payment by id. Restricted to owners of the payment, which includes the payer and the payee

Response
Returns a Payment

Arguments
Name	Description
id - ID!	
Example
Query
query payment($id: ID!) {
  payment(id: $id) {
    amount
    chargeId
    createdAt
    currency
    directCharge
    entries {
      ...EntryFragment
    }
    fee
    id
    intentId
    payable {
      ... on Event {
        ...EventFragment
      }
      ... on Series {
        ...SeriesFragment
      }
    }
    purchasedOptions {
      ...PurchasedOptionsFragment
    }
    refunds {
      ...RefundFragment
    }
    registrationError
    status
    user {
      ...UserFragment
    }
  }
}
Variables
{"id": 4}
Response
{
  "data": {
    "payment": {
      "amount": 123,
      "chargeId": "xyz789",
      "createdAt": ISO8601DateTime,
      "currency": "xyz789",
      "directCharge": false,
      "entries": [Entry],
      "fee": 123,
      "id": "4",
      "intentId": "abc123",
      "payable": Event,
      "purchasedOptions": PurchasedOptions,
      "refunds": [Refund],
      "registrationError": "xyz789",
      "status": "abc123",
      "user": User
    }
  }
}
Queries
physicalTag
Description
Get a physical tag by it's id

Response
Returns a PhysicalTag

Arguments
Name	Description
id - ID	
humanReadableId - ID	
Example
Query
query physicalTag(
  $id: ID,
  $humanReadableId: ID
) {
  physicalTag(
    id: $id,
    humanReadableId: $humanReadableId
  ) {
    athlete {
      ...AthleteFragment
    }
    athleteId
    humanReadableId
    id
  }
}
Variables
{"id": 4, "humanReadableId": "4"}
Response
{
  "data": {
    "physicalTag": {
      "athlete": Athlete,
      "athleteId": "4",
      "humanReadableId": "4",
      "id": 4
    }
  }
}
Queries
pricingData
Description
Get the pricing data

Response
Returns a PricingData!

Example
Query
query pricingData {
  pricingData {
    addOnBaselinePrices {
      ...AddOnBaselinePriceFragment
    }
    country
    creditBaselinePrices {
      ...CreditBaselinePriceFragment
    }
    currency
    marketFactors {
      ...MarketFactorFragment
    }
    region
    sizeFactors {
      ...SizeFactorFragment
    }
    volumeDiscounts
  }
}
Response
{
  "data": {
    "pricingData": {
      "addOnBaselinePrices": [AddOnBaselinePrice],
      "country": "xyz789",
      "creditBaselinePrices": [CreditBaselinePrice],
      "currency": "xyz789",
      "marketFactors": [MarketFactor],
      "region": "abc123",
      "sizeFactors": [SizeFactor],
      "volumeDiscounts": [987.65]
    }
  }
}
Queries
series
Description
Get a series by it's id

Response
Returns a Series

Arguments
Name	Description
id - ID!	
Example
Query
query series($id: ID!) {
  series(id: $id) {
    allDivisions {
      ...DivisionFragment
    }
    athleteRankingResults {
      ...AthleteRankingResultFragment
    }
    availableRankingFilters
    captureFields {
      ...PropertyFragment
    }
    childSeries {
      ...SeriesFragment
    }
    divisions {
      ...DivisionFragment
    }
    events {
      ...EventFragment
    }
    exclusive
    id
    membershipDivisions {
      ...DivisionFragment
    }
    name
    options {
      ...OptionsFragment
    }
    organisation {
      ...OrganisationFragment
    }
    organisationId
    paginatedMemberships {
      ...MembershipsFragment
    }
    parentSeries {
      ...SeriesFragment
    }
    pointAllocationId
    rankingOptions {
      ...RankingOptionsFragment
    }
    rankings {
      ...SeriesRankFragment
    }
    rankingsDisplayProperty
    rankingsDivisions {
      ...DivisionFragment
    }
    registrationOptions {
      ...RegistrationOptionsFragment
    }
    results {
      ...ResultFragment
    }
    resultsToCount
    signOnStatus
  }
}
Variables
{"id": 4}
Response
{
  "data": {
    "series": {
      "allDivisions": [Division],
      "athleteRankingResults": AthleteRankingResult,
      "availableRankingFilters": ["xyz789"],
      "captureFields": [Property],
      "childSeries": [Series],
      "divisions": [Division],
      "events": [Event],
      "exclusive": false,
      "id": "4",
      "membershipDivisions": [Division],
      "name": "abc123",
      "options": Options,
      "organisation": Organisation,
      "organisationId": 4,
      "paginatedMemberships": Memberships,
      "parentSeries": Series,
      "pointAllocationId": 4,
      "rankingOptions": RankingOptions,
      "rankings": [SeriesRank],
      "rankingsDisplayProperty": {},
      "rankingsDivisions": [Division],
      "registrationOptions": RegistrationOptions,
      "results": [Result],
      "resultsToCount": {},
      "signOnStatus": "closed"
    }
  }
}
Queries
seriesRankingRuleOverride
Description
Get ranking rule overrides by series id and rule

Response
Returns [RankingRuleOverride!]

Arguments
Name	Description
seriesId - ID!	
rule - String!	
Example
Query
query seriesRankingRuleOverride(
  $seriesId: ID!,
  $rule: String!
) {
  seriesRankingRuleOverride(
    seriesId: $seriesId,
    rule: $rule
  ) {
    athlete {
      ...AthleteFragment
    }
    division {
      ...DivisionFragment
    }
    id
    override
    rule
    series {
      ...SeriesFragment
    }
  }
}
Variables
{
  "seriesId": "4",
  "rule": "abc123"
}
Response
{
  "data": {
    "seriesRankingRuleOverride": [
      {
        "athlete": Athlete,
        "division": Division,
        "id": "4",
        "override": 123,
        "rule": "abc123",
        "series": Series
      }
    ]
  }
}
Queries
shortNameAvailable
Description
Check if a short name candidate is available for an organisation

Response
Returns a Boolean!

Arguments
Name	Description
shortName - String	
organisationId - ID	
Example
Query
query shortNameAvailable(
  $shortName: String,
  $organisationId: ID
) {
  shortNameAvailable(
    shortName: $shortName,
    organisationId: $organisationId
  )
}
Variables
{
  "shortName": "xyz789",
  "organisationId": "4"
}
Response
{"data": {"shortNameAvailable": false}}
Queries
stripeClientId
Description
Get the public Stripe client id for the current environment

Response
Returns a String!

Example
Query
query stripeClientId {
  stripeClientId
}
Response
{"data": {"stripeClientId": "xyz789"}}
Queries
user
Description
Get the current user

Response
Returns a User

Example
Query
query user {
  user {
    athletes {
      ...AthleteFragment
    }
    competitors {
      ...CompetitorFragment
    }
    email
    entries {
      ...EntryFragment
    }
    eventAthletes {
      ...AthleteFragment
    }
    eventEmails {
      ...EmailFragment
    }
    id
    image
    name
    pendingPayments {
      ...PaymentFragment
    }
    phone
    properties
    role
    unfinishedEvents {
      ...EventFragment
    }
  }
}
Response
{
  "data": {
    "user": {
      "athletes": [Athlete],
      "competitors": [Competitor],
      "email": "xyz789",
      "entries": [Entry],
      "eventAthletes": [Athlete],
      "eventEmails": [Email],
      "id": 4,
      "image": "xyz789",
      "name": "abc123",
      "pendingPayments": [Payment],
      "phone": "abc123",
      "properties": {},
      "role": "abc123",
      "unfinishedEvents": [Event]
    }
  }
}
Mutations
addAthleteToHeat
Response
Returns an AddAthleteToHeatPayload

Arguments
Name	Description
input - AddAthleteToHeatInput!	Parameters for AddAthleteToHeat
Example
Query
mutation addAthleteToHeat($input: AddAthleteToHeatInput!) {
  addAthleteToHeat(input: $input) {
    clientMutationId
    heat {
      ...HeatFragment
    }
  }
}
Variables
{"input": AddAthleteToHeatInput}
Response
{
  "data": {
    "addAthleteToHeat": {
      "clientMutationId": "xyz789",
      "heat": Heat
    }
  }
}
Mutations
addHeatToRound
Response
Returns an AddHeatToRoundPayload

Arguments
Name	Description
input - AddHeatToRoundInput!	Parameters for AddHeatToRound
Example
Query
mutation addHeatToRound($input: AddHeatToRoundInput!) {
  addHeatToRound(input: $input) {
    clientMutationId
    heat {
      ...HeatFragment
    }
  }
}
Variables
{"input": AddHeatToRoundInput}
Response
{
  "data": {
    "addHeatToRound": {
      "clientMutationId": "xyz789",
      "heat": Heat
    }
  }
}
Mutations
addPermissionToRecord
Response
Returns an AddPermissionToRecordPayload

Arguments
Name	Description
input - AddPermissionToRecordInput!	Parameters for AddPermissionToRecord
Example
Query
mutation addPermissionToRecord($input: AddPermissionToRecordInput!) {
  addPermissionToRecord(input: $input) {
    clientMutationId
    record {
      ... on Team {
        ...TeamFragment
      }
    }
    user {
      ...UserFragment
    }
  }
}
Variables
{"input": AddPermissionToRecordInput}
Response
{
  "data": {
    "addPermissionToRecord": {
      "clientMutationId": "abc123",
      "record": Team,
      "user": User
    }
  }
}
Mutations
addPriority
Response
Returns an AddPriorityPayload

Arguments
Name	Description
input - AddPriorityInput!	Parameters for AddPriority
Example
Query
mutation addPriority($input: AddPriorityInput!) {
  addPriority(input: $input) {
    clientMutationId
    heat {
      ...HeatFragment
    }
  }
}
Variables
{"input": AddPriorityInput}
Response
{
  "data": {
    "addPriority": {
      "clientMutationId": "abc123",
      "heat": Heat
    }
  }
}
Mutations
addRankingRuleOverride
Description
creates a ranking rule override for an athlete.

Response
Returns an AddRankingRuleOverridePayload

Arguments
Name	Description
input - AddRankingRuleOverrideInput!	Parameters for AddRankingRuleOverride
Example
Query
mutation addRankingRuleOverride($input: AddRankingRuleOverrideInput!) {
  addRankingRuleOverride(input: $input) {
    clientMutationId
    rankingRuleOverride {
      ...RankingRuleOverrideFragment
    }
  }
}
Variables
{"input": AddRankingRuleOverrideInput}
Response
{
  "data": {
    "addRankingRuleOverride": {
      "clientMutationId": "xyz789",
      "rankingRuleOverride": RankingRuleOverride
    }
  }
}
Mutations
addRound
Response
Returns an AddRoundPayload

Arguments
Name	Description
input - AddRoundInput!	Parameters for AddRound
Example
Query
mutation addRound($input: AddRoundInput!) {
  addRound(input: $input) {
    clientMutationId
    eventDivision {
      ...EventDivisionFragment
    }
  }
}
Variables
{"input": AddRoundInput}
Response
{
  "data": {
    "addRound": {
      "clientMutationId": "abc123",
      "eventDivision": EventDivision
    }
  }
}
Mutations
addUserToAthlete
Response
Returns an AddUserToAthletePayload

Arguments
Name	Description
input - AddUserToAthleteInput!	Parameters for AddUserToAthlete
Example
Query
mutation addUserToAthlete($input: AddUserToAthleteInput!) {
  addUserToAthlete(input: $input) {
    clientMutationId
    user {
      ...UserFragment
    }
  }
}
Variables
{"input": AddUserToAthleteInput}
Response
{
  "data": {
    "addUserToAthlete": {
      "clientMutationId": "abc123",
      "user": User
    }
  }
}
Mutations
addUserToOrganisation
Response
Returns an AddUserToOrganisationPayload

Arguments
Name	Description
input - AddUserToOrganisationInput!	Parameters for AddUserToOrganisation
Example
Query
mutation addUserToOrganisation($input: AddUserToOrganisationInput!) {
  addUserToOrganisation(input: $input) {
    clientMutationId
    user {
      ...UserFragment
    }
  }
}
Variables
{"input": AddUserToOrganisationInput}
Response
{
  "data": {
    "addUserToOrganisation": {
      "clientMutationId": "xyz789",
      "user": User
    }
  }
}
Mutations
appendChildContest
Response
Returns an AppendChildContestPayload

Arguments
Name	Description
input - AppendChildContestInput!	Parameters for AppendChildContest
Example
Query
mutation appendChildContest($input: AppendChildContestInput!) {
  appendChildContest(input: $input) {
    clientMutationId
    eventDivision {
      ...EventDivisionFragment
    }
  }
}
Variables
{"input": AppendChildContestInput}
Response
{
  "data": {
    "appendChildContest": {
      "clientMutationId": "abc123",
      "eventDivision": EventDivision
    }
  }
}
Mutations
archiveOrganisationProperty
Response
Returns an ArchiveOrganisationPropertyPayload

Arguments
Name	Description
input - ArchiveOrganisationPropertyInput!	Parameters for ArchiveOrganisationProperty
Example
Query
mutation archiveOrganisationProperty($input: ArchiveOrganisationPropertyInput!) {
  archiveOrganisationProperty(input: $input) {
    clientMutationId
    property {
      ...PropertyFragment
    }
  }
}
Variables
{"input": ArchiveOrganisationPropertyInput}
Response
{
  "data": {
    "archiveOrganisationProperty": {
      "clientMutationId": "xyz789",
      "property": Property
    }
  }
}
Mutations
cancelEntry
Description
Cancel an entry in a division

Response
Returns a CancelEntryPayload

Arguments
Name	Description
input - CancelEntryInput!	Parameters for CancelEntry
Example
Query
mutation cancelEntry($input: CancelEntryInput!) {
  cancelEntry(input: $input) {
    clientMutationId
    entry {
      ...EntryFragment
    }
  }
}
Variables
{"input": CancelEntryInput}
Response
{
  "data": {
    "cancelEntry": {
      "clientMutationId": "abc123",
      "entry": Entry
    }
  }
}
Mutations
copyEvent
Description
Creates a new event from copy of an event inside the organisation referenced on the organisationId argument. The caller must have events/director scope permissions for that organisation.

Response
Returns a CopyEventPayload

Arguments
Name	Description
input - CopyEventInput!	Parameters for CopyEvent
Example
Query
mutation copyEvent($input: CopyEventInput!) {
  copyEvent(input: $input) {
    clientMutationId
    event {
      ...EventFragment
    }
  }
}
Variables
{"input": CopyEventInput}
Response
{
  "data": {
    "copyEvent": {
      "clientMutationId": "abc123",
      "event": Event
    }
  }
}
Mutations
createEntries
Description
Creates the provided entries in the event associated to the eventId argument. The caller must have events/director scope permissions for that event.

Response
Returns a CreateEntriesPayload

Arguments
Name	Description
input - CreateEntriesInput!	Parameters for CreateEntries
Example
Query
mutation createEntries($input: CreateEntriesInput!) {
  createEntries(input: $input) {
    clientMutationId
    entries {
      ...EntryFragment
    }
  }
}
Variables
{"input": CreateEntriesInput}
Response
{
  "data": {
    "createEntries": {
      "clientMutationId": "xyz789",
      "entries": [Entry]
    }
  }
}
Mutations
createEvent
Description
Creates a new event inside the organisation referenced on the organisationId argument. The caller must have events/director scope permissions for that organisation.

Response
Returns a CreateEventPayload

Arguments
Name	Description
input - CreateEventInput!	Parameters for CreateEvent
Example
Query
mutation createEvent($input: CreateEventInput!) {
  createEvent(input: $input) {
    clientMutationId
    event {
      ...EventFragment
    }
  }
}
Variables
{"input": CreateEventInput}
Response
{
  "data": {
    "createEvent": {
      "clientMutationId": "xyz789",
      "event": Event
    }
  }
}
Mutations
createMembership
Description
creates a membership for an athlete.

Response
Returns a CreateMembershipPayload

Arguments
Name	Description
input - CreateMembershipInput!	Parameters for CreateMembership
Example
Query
mutation createMembership($input: CreateMembershipInput!) {
  createMembership(input: $input) {
    clientMutationId
    membership {
      ...MembershipFragment
    }
  }
}
Variables
{"input": CreateMembershipInput}
Response
{
  "data": {
    "createMembership": {
      "clientMutationId": "xyz789",
      "membership": Membership
    }
  }
}
Mutations
createOrganisation
Response
Returns a CreateOrganisationPayload

Arguments
Name	Description
input - CreateOrganisationInput!	Parameters for CreateOrganisation
Example
Query
mutation createOrganisation($input: CreateOrganisationInput!) {
  createOrganisation(input: $input) {
    clientMutationId
    organisation {
      ...OrganisationFragment
    }
  }
}
Variables
{"input": CreateOrganisationInput}
Response
{
  "data": {
    "createOrganisation": {
      "clientMutationId": "xyz789",
      "organisation": Organisation
    }
  }
}
Mutations
createOrganisationProperty
Response
Returns a CreateOrganisationPropertyPayload

Arguments
Name	Description
input - CreateOrganisationPropertyInput!	Parameters for CreateOrganisationProperty
Example
Query
mutation createOrganisationProperty($input: CreateOrganisationPropertyInput!) {
  createOrganisationProperty(input: $input) {
    clientMutationId
    property {
      ...PropertyFragment
    }
  }
}
Variables
{"input": CreateOrganisationPropertyInput}
Response
{
  "data": {
    "createOrganisationProperty": {
      "clientMutationId": "xyz789",
      "property": Property
    }
  }
}
Mutations
deleteContest
Response
Returns a DeleteContestPayload

Arguments
Name	Description
input - DeleteContestInput!	Parameters for DeleteContest
Example
Query
mutation deleteContest($input: DeleteContestInput!) {
  deleteContest(input: $input) {
    clientMutationId
    eventDivision {
      ...EventDivisionFragment
    }
  }
}
Variables
{"input": DeleteContestInput}
Response
{
  "data": {
    "deleteContest": {
      "clientMutationId": "xyz789",
      "eventDivision": EventDivision
    }
  }
}
Mutations
deleteHeat
Response
Returns a DeleteHeatPayload

Arguments
Name	Description
input - DeleteHeatInput!	Parameters for DeleteHeat
Example
Query
mutation deleteHeat($input: DeleteHeatInput!) {
  deleteHeat(input: $input) {
    clientMutationId
    eventDivision {
      ...EventDivisionFragment
    }
    heat {
      ...HeatFragment
    }
  }
}
Variables
{"input": DeleteHeatInput}
Response
{
  "data": {
    "deleteHeat": {
      "clientMutationId": "abc123",
      "eventDivision": EventDivision,
      "heat": Heat
    }
  }
}
Mutations
deleteMembership
Description
delete a membership

Response
Returns a DeleteMembershipPayload

Arguments
Name	Description
input - DeleteMembershipInput!	Parameters for DeleteMembership
Example
Query
mutation deleteMembership($input: DeleteMembershipInput!) {
  deleteMembership(input: $input) {
    clientMutationId
    membership {
      ...MembershipFragment
    }
  }
}
Variables
{"input": DeleteMembershipInput}
Response
{
  "data": {
    "deleteMembership": {
      "clientMutationId": "abc123",
      "membership": Membership
    }
  }
}
Mutations
deleteRankingRuleOverride
Description
delete a ranking rule ovveride for an athlete

Response
Returns a DeleteRankingRuleOverridePayload

Arguments
Name	Description
input - DeleteRankingRuleOverrideInput!	Parameters for DeleteRankingRuleOverride
Example
Query
mutation deleteRankingRuleOverride($input: DeleteRankingRuleOverrideInput!) {
  deleteRankingRuleOverride(input: $input) {
    clientMutationId
    rankingRuleOverride {
      ...RankingRuleOverrideFragment
    }
  }
}
Variables
{"input": DeleteRankingRuleOverrideInput}
Response
{
  "data": {
    "deleteRankingRuleOverride": {
      "clientMutationId": "xyz789",
      "rankingRuleOverride": RankingRuleOverride
    }
  }
}
Mutations
deleteSeries
Description
Soft-delete a series

Response
Returns a DeleteSeriesPayload

Arguments
Name	Description
input - DeleteSeriesInput!	Parameters for DeleteSeries
Example
Query
mutation deleteSeries($input: DeleteSeriesInput!) {
  deleteSeries(input: $input) {
    clientMutationId
    series {
      ...SeriesFragment
    }
  }
}
Variables
{"input": DeleteSeriesInput}
Response
{
  "data": {
    "deleteSeries": {
      "clientMutationId": "abc123",
      "series": Series
    }
  }
}
Mutations
excludeAthleteFromRankings
Description
Excludes an athlete from all series rankings for the event division

Response
Returns an ExcludeAthleteFromRankingsPayload

Arguments
Name	Description
input - ExcludeAthleteFromRankingsInput!	Parameters for ExcludeAthleteFromRankings
Example
Query
mutation excludeAthleteFromRankings($input: ExcludeAthleteFromRankingsInput!) {
  excludeAthleteFromRankings(input: $input) {
    clientMutationId
    eventDivision {
      ...EventDivisionFragment
    }
  }
}
Variables
{"input": ExcludeAthleteFromRankingsInput}
Response
{
  "data": {
    "excludeAthleteFromRankings": {
      "clientMutationId": "abc123",
      "eventDivision": EventDivision
    }
  }
}
Mutations
linkTagToAthlete
Response
Returns a LinkTagToAthletePayload

Arguments
Name	Description
input - LinkTagToAthleteInput!	Parameters for LinkTagToAthlete
Example
Query
mutation linkTagToAthlete($input: LinkTagToAthleteInput!) {
  linkTagToAthlete(input: $input) {
    clientMutationId
    tag {
      ...PhysicalTagFragment
    }
  }
}
Variables
{"input": LinkTagToAthleteInput}
Response
{
  "data": {
    "linkTagToAthlete": {
      "clientMutationId": "xyz789",
      "tag": PhysicalTag
    }
  }
}
Mutations
mergeAthletes
Response
Returns a MergeAthletesPayload

Arguments
Name	Description
input - MergeAthletesInput!	Parameters for MergeAthletes
Example
Query
mutation mergeAthletes($input: MergeAthletesInput!) {
  mergeAthletes(input: $input) {
    athlete {
      ...AthleteFragment
    }
    clientMutationId
  }
}
Variables
{"input": MergeAthletesInput}
Response
{
  "data": {
    "mergeAthletes": {
      "athlete": Athlete,
      "clientMutationId": "abc123"
    }
  }
}
Mutations
moveHeatItems
Response
Returns a MoveHeatItemsPayload

Arguments
Name	Description
input - MoveHeatItemsInput!	Parameters for MoveHeatItems
Example
Query
mutation moveHeatItems($input: MoveHeatItemsInput!) {
  moveHeatItems(input: $input) {
    clientMutationId
    heats {
      ...HeatFragment
    }
  }
}
Variables
{"input": MoveHeatItemsInput}
Response
{
  "data": {
    "moveHeatItems": {
      "clientMutationId": "xyz789",
      "heats": [Heat]
    }
  }
}
Mutations
refundPayment
Response
Returns a RefundPaymentPayload

Arguments
Name	Description
input - RefundPaymentInput!	Parameters for RefundPayment
Example
Query
mutation refundPayment($input: RefundPaymentInput!) {
  refundPayment(input: $input) {
    clientMutationId
    errors
    payment {
      ...PaymentFragment
    }
  }
}
Variables
{"input": RefundPaymentInput}
Response
{
  "data": {
    "refundPayment": {
      "clientMutationId": "abc123",
      "errors": "abc123",
      "payment": Payment
    }
  }
}
Mutations
removeAthleteFromHeat
Response
Returns a RemoveAthleteFromHeatPayload

Arguments
Name	Description
input - RemoveAthleteFromHeatInput!	Parameters for RemoveAthleteFromHeat
Example
Query
mutation removeAthleteFromHeat($input: RemoveAthleteFromHeatInput!) {
  removeAthleteFromHeat(input: $input) {
    clientMutationId
    heat {
      ...HeatFragment
    }
  }
}
Variables
{"input": RemoveAthleteFromHeatInput}
Response
{
  "data": {
    "removeAthleteFromHeat": {
      "clientMutationId": "abc123",
      "heat": Heat
    }
  }
}
Mutations
removePermissionFromRecord
Response
Returns a RemovePermissionFromRecordPayload

Arguments
Name	Description
input - RemovePermissionFromRecordInput!	Parameters for RemovePermissionFromRecord
Example
Query
mutation removePermissionFromRecord($input: RemovePermissionFromRecordInput!) {
  removePermissionFromRecord(input: $input) {
    clientMutationId
    team {
      ...TeamFragment
    }
  }
}
Variables
{"input": RemovePermissionFromRecordInput}
Response
{
  "data": {
    "removePermissionFromRecord": {
      "clientMutationId": "xyz789",
      "team": Team
    }
  }
}
Mutations
removePriority
Response
Returns a RemovePriorityPayload

Arguments
Name	Description
input - RemovePriorityInput!	Parameters for RemovePriority
Example
Query
mutation removePriority($input: RemovePriorityInput!) {
  removePriority(input: $input) {
    clientMutationId
    heat {
      ...HeatFragment
    }
  }
}
Variables
{"input": RemovePriorityInput}
Response
{
  "data": {
    "removePriority": {
      "clientMutationId": "abc123",
      "heat": Heat
    }
  }
}
Mutations
removeUserFromOrganisation
Response
Returns a RemoveUserFromOrganisationPayload

Arguments
Name	Description
input - RemoveUserFromOrganisationInput!	Parameters for RemoveUserFromOrganisation
Example
Query
mutation removeUserFromOrganisation($input: RemoveUserFromOrganisationInput!) {
  removeUserFromOrganisation(input: $input) {
    clientMutationId
    user {
      ...UserFragment
    }
  }
}
Variables
{"input": RemoveUserFromOrganisationInput}
Response
{
  "data": {
    "removeUserFromOrganisation": {
      "clientMutationId": "abc123",
      "user": User
    }
  }
}
Mutations
resetUserPassword
Response
Returns a ResetUserPasswordPayload

Arguments
Name	Description
input - ResetUserPasswordInput!	Parameters for ResetUserPassword
Example
Query
mutation resetUserPassword($input: ResetUserPasswordInput!) {
  resetUserPassword(input: $input) {
    clientMutationId
    user {
      ...UserFragment
    }
  }
}
Variables
{"input": ResetUserPasswordInput}
Response
{
  "data": {
    "resetUserPassword": {
      "clientMutationId": "abc123",
      "user": User
    }
  }
}
Mutations
saveEventDivisionAsTemplate
Description
Saves the configurations of the eventDivision as a new template with the provided name on the provided organisation. The caller must have organisations/manage scope permissions for that organisation and events/director for the event the eventDivision belongs to.

Response
Returns a SaveEventDivisionAsTemplatePayload

Arguments
Name	Description
input - SaveEventDivisionAsTemplateInput!	Parameters for SaveEventDivisionAsTemplate
Example
Query
mutation saveEventDivisionAsTemplate($input: SaveEventDivisionAsTemplateInput!) {
  saveEventDivisionAsTemplate(input: $input) {
    clientMutationId
    eventDivision {
      ...EventDivisionFragment
    }
  }
}
Variables
{"input": SaveEventDivisionAsTemplateInput}
Response
{
  "data": {
    "saveEventDivisionAsTemplate": {
      "clientMutationId": "xyz789",
      "eventDivision": EventDivision
    }
  }
}
Mutations
sendEventEmail
Description
Send an event email to a list of recipients

Response
Returns a SendEventEmailPayload

Arguments
Name	Description
input - SendEventEmailInput!	Parameters for SendEventEmail
Example
Query
mutation sendEventEmail($input: SendEventEmailInput!) {
  sendEventEmail(input: $input) {
    clientMutationId
    event {
      ...EventFragment
    }
  }
}
Variables
{"input": SendEventEmailInput}
Response
{
  "data": {
    "sendEventEmail": {
      "clientMutationId": "xyz789",
      "event": Event
    }
  }
}
Mutations
updateAthlete
Response
Returns an UpdateAthletePayload

Arguments
Name	Description
input - UpdateAthleteInput!	Parameters for UpdateAthlete
Example
Query
mutation updateAthlete($input: UpdateAthleteInput!) {
  updateAthlete(input: $input) {
    athlete {
      ...AthleteFragment
    }
    clientMutationId
  }
}
Variables
{"input": UpdateAthleteInput}
Response
{
  "data": {
    "updateAthlete": {
      "athlete": Athlete,
      "clientMutationId": "xyz789"
    }
  }
}
Mutations
updateContest
Response
Returns an UpdateContestPayload

Arguments
Name	Description
input - UpdateContestInput!	Parameters for UpdateContest
Example
Query
mutation updateContest($input: UpdateContestInput!) {
  updateContest(input: $input) {
    clientMutationId
    contest {
      ...ContestFragment
    }
    eventDivision {
      ...EventDivisionFragment
    }
  }
}
Variables
{"input": UpdateContestInput}
Response
{
  "data": {
    "updateContest": {
      "clientMutationId": "abc123",
      "contest": Contest,
      "eventDivision": EventDivision
    }
  }
}
Mutations
updateEventConfig
Response
Returns an UpdateEventConfigPayload

Arguments
Name	Description
input - UpdateEventConfigInput!	Parameters for UpdateEventConfig
Example
Query
mutation updateEventConfig($input: UpdateEventConfigInput!) {
  updateEventConfig(input: $input) {
    clientMutationId
    event {
      ...EventFragment
    }
  }
}
Variables
{"input": UpdateEventConfigInput}
Response
{
  "data": {
    "updateEventConfig": {
      "clientMutationId": "xyz789",
      "event": Event
    }
  }
}
Mutations
updateEventDivision
Response
Returns an UpdateEventDivisionPayload

Arguments
Name	Description
input - UpdateEventDivisionInput!	Parameters for UpdateEventDivision
Example
Query
mutation updateEventDivision($input: UpdateEventDivisionInput!) {
  updateEventDivision(input: $input) {
    clientMutationId
    eventDivision {
      ...EventDivisionFragment
    }
  }
}
Variables
{"input": UpdateEventDivisionInput}
Response
{
  "data": {
    "updateEventDivision": {
      "clientMutationId": "xyz789",
      "eventDivision": EventDivision
    }
  }
}
Mutations
updateMembership
Description
updates a membership.

Response
Returns an UpdateMembershipPayload

Arguments
Name	Description
input - UpdateMembershipInput!	Parameters for UpdateMembership
Example
Query
mutation updateMembership($input: UpdateMembershipInput!) {
  updateMembership(input: $input) {
    clientMutationId
    membership {
      ...MembershipFragment
    }
  }
}
Variables
{"input": UpdateMembershipInput}
Response
{
  "data": {
    "updateMembership": {
      "clientMutationId": "abc123",
      "membership": Membership
    }
  }
}
Mutations
updateOrganisation
Response
Returns an UpdateOrganisationPayload

Arguments
Name	Description
input - UpdateOrganisationInput!	Parameters for UpdateOrganisation
Example
Query
mutation updateOrganisation($input: UpdateOrganisationInput!) {
  updateOrganisation(input: $input) {
    clientMutationId
    organisation {
      ...OrganisationFragment
    }
  }
}
Variables
{"input": UpdateOrganisationInput}
Response
{
  "data": {
    "updateOrganisation": {
      "clientMutationId": "abc123",
      "organisation": Organisation
    }
  }
}
Mutations
updateRankingRuleOverride
Description
updates a ranking rule override for an athlete.

Response
Returns an UpdateRankingRuleOverridePayload

Arguments
Name	Description
input - UpdateRankingRuleOverrideInput!	Parameters for UpdateRankingRuleOverride
Example
Query
mutation updateRankingRuleOverride($input: UpdateRankingRuleOverrideInput!) {
  updateRankingRuleOverride(input: $input) {
    clientMutationId
    rankingRuleOverride {
      ...RankingRuleOverrideFragment
    }
  }
}
Variables
{"input": UpdateRankingRuleOverrideInput}
Response
{
  "data": {
    "updateRankingRuleOverride": {
      "clientMutationId": "xyz789",
      "rankingRuleOverride": RankingRuleOverride
    }
  }
}
Mutations
updateRound
Response
Returns an UpdateRoundPayload

Arguments
Name	Description
input - UpdateRoundInput!	Parameters for UpdateRound
Example
Query
mutation updateRound($input: UpdateRoundInput!) {
  updateRound(input: $input) {
    clientMutationId
    heats {
      ...HeatFragment
    }
  }
}
Variables
{"input": UpdateRoundInput}
Response
{
  "data": {
    "updateRound": {
      "clientMutationId": "abc123",
      "heats": [Heat]
    }
  }
}
Mutations
updateTeamMembers
Description
Adds or removes team members from a team. The caller must be the owner of the team and the team member

Response
Returns an UpdateTeamMembersPayload

Arguments
Name	Description
input - UpdateTeamMembersInput!	Parameters for UpdateTeamMembers
Example
Query
mutation updateTeamMembers($input: UpdateTeamMembersInput!) {
  updateTeamMembers(input: $input) {
    athleteHeats {
      ...CompetitorFragment
    }
    clientMutationId
    entry {
      ...EntryFragment
    }
  }
}
Variables
{"input": UpdateTeamMembersInput}
Response
{
  "data": {
    "updateTeamMembers": {
      "athleteHeats": [Competitor],
      "clientMutationId": "abc123",
      "entry": Entry
    }
  }
}
Types
AccountAddOnsPurchase
Fields
Field Name	Description
customTemplates - ISO8601DateTime	
documentSigning - ISO8601DateTime	
embed - ISO8601DateTime	
whatsAppSupport - ISO8601DateTime	
Example
{
  "customTemplates": ISO8601DateTime,
  "documentSigning": ISO8601DateTime,
  "embed": ISO8601DateTime,
  "whatsAppSupport": ISO8601DateTime
}
Types
ActivePurchases
Fields
Field Name	Description
accountAddOns - AccountAddOnsPurchase	
eventAddOns - EventAddOnsPurchase	
eventCredits - EventCreditsPurchase	
Example
{
  "accountAddOns": AccountAddOnsPurchase,
  "eventAddOns": EventAddOnsPurchase,
  "eventCredits": EventCreditsPurchase
}
Types
AddAthleteToHeatInput
Description
Autogenerated input type of AddAthleteToHeat

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heatId - ID!	
eventDivisionId - ID	
athleteHeat - AthleteHeatInput!	
Example
{
  "clientMutationId": "xyz789",
  "heatId": "4",
  "eventDivisionId": 4,
  "athleteHeat": AthleteHeatInput
}
Types
AddAthleteToHeatPayload
Description
Autogenerated return type of AddAthleteToHeat.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heat - Heat!	
Example
{
  "clientMutationId": "xyz789",
  "heat": Heat
}
Types
AddHeatToRoundInput
Description
Autogenerated input type of AddHeatToRound

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivisionId - ID!	
roundPosition - Int!	
Example
{
  "clientMutationId": "xyz789",
  "eventDivisionId": "4",
  "roundPosition": 123
}
Types
AddHeatToRoundPayload
Description
Autogenerated return type of AddHeatToRound.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heat - Heat!	
Example
{
  "clientMutationId": "xyz789",
  "heat": Heat
}
Types
AddOnBaselinePrice
Fields
Field Name	Description
name - String!	
price - Int!	
type - String!	
Example
{
  "name": "abc123",
  "price": 123,
  "type": "abc123"
}
Types
AddPermissionToRecordInput
Description
Autogenerated input type of AddPermissionToRecord

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
permission - PermissionInput!	
organisationId - ID!	
Example
{
  "clientMutationId": "abc123",
  "permission": PermissionInput,
  "organisationId": "4"
}
Types
AddPermissionToRecordPayload
Description
Autogenerated return type of AddPermissionToRecord.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
record - Record!	
user - User!	
Example
{
  "clientMutationId": "xyz789",
  "record": Team,
  "user": User
}
Types
AddPriorityInput
Description
Autogenerated input type of AddPriority

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
competitorId - ID!	
priority - Int!	
Example
{
  "clientMutationId": "xyz789",
  "competitorId": 4,
  "priority": 123
}
Types
AddPriorityPayload
Description
Autogenerated return type of AddPriority.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heat - Heat!	
Example
{
  "clientMutationId": "xyz789",
  "heat": Heat
}
Types
AddRankingRuleOverrideInput
Description
Autogenerated input type of AddRankingRuleOverride

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
rankingRuleOverride - RankingRuleOverrideInput!	
Example
{
  "clientMutationId": "abc123",
  "rankingRuleOverride": RankingRuleOverrideInput
}
Types
AddRankingRuleOverridePayload
Description
Autogenerated return type of AddRankingRuleOverride.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
rankingRuleOverride - RankingRuleOverride!	
Example
{
  "clientMutationId": "xyz789",
  "rankingRuleOverride": RankingRuleOverride
}
Types
AddRoundInput
Description
Autogenerated input type of AddRound

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivisionId - ID!	
Example
{
  "clientMutationId": "xyz789",
  "eventDivisionId": 4
}
Types
AddRoundPayload
Description
Autogenerated return type of AddRound.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivision - EventDivision!	
Example
{
  "clientMutationId": "abc123",
  "eventDivision": EventDivision
}
Types
AddUserToAthleteInput
Description
Autogenerated input type of AddUserToAthlete

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
athleteId - ID!	
name - String!	
email - String!	
phone - String	
Example
{
  "clientMutationId": "xyz789",
  "athleteId": 4,
  "name": "xyz789",
  "email": "abc123",
  "phone": "abc123"
}
Types
AddUserToAthletePayload
Description
Autogenerated return type of AddUserToAthlete.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
user - User!	
Example
{
  "clientMutationId": "abc123",
  "user": User
}
Types
AddUserToOrganisationInput
Description
Autogenerated input type of AddUserToOrganisation

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
userDetails - OrganisationUserInput!	
Example
{
  "clientMutationId": "abc123",
  "userDetails": OrganisationUserInput
}
Types
AddUserToOrganisationPayload
Description
Autogenerated return type of AddUserToOrganisation.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
user - User!	
Example
{
  "clientMutationId": "xyz789",
  "user": User
}
Types
AppendChildContestInput
Description
Autogenerated input type of AppendChildContest

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
contestId - ID!	
Example
{
  "clientMutationId": "abc123",
  "contestId": 4
}
Types
AppendChildContestPayload
Description
Autogenerated return type of AppendChildContest.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivision - EventDivision!	
Example
{
  "clientMutationId": "abc123",
  "eventDivision": EventDivision
}
Types
ArchiveOrganisationPropertyInput
Description
Autogenerated input type of ArchiveOrganisationProperty

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
uuid - String!	
Example
{
  "clientMutationId": "xyz789",
  "id": "4",
  "uuid": "xyz789"
}
Types
ArchiveOrganisationPropertyPayload
Description
Autogenerated return type of ArchiveOrganisationProperty.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
property - Property!	
Example
{
  "clientMutationId": "abc123",
  "property": Property
}
Types
Athlete
Fields
Field Name	Description
appearances - [Competitor!]	
Arguments
eventId - ID
eventDivisionId - ID
createdAt - ISO8601Date!	
dob - ISO8601Date	
entries - [AthleteEntry!]	
Arguments
eventId - ID
eventDivisionId - ID
entriesWithPendingPayments - [Entry!]!	
eventDivisions - [EventDivision!]!	
Arguments
limit - Int
id - ID!	
image - String	Image URL with an implicit max-width. Accepts any number > 0 for size in pixels or "original" for the original image
Arguments
size - StringOrInteger
memberships - [AthleteMembership!]!	
name - String!	
nationality - String	
physicalTags - [PhysicalTag!]!	
properties - JSON	
ranks - [EventDivisionRank!]	
unfinishedEvents - [Event!]!	
updatedAt - ISO8601Date!	
users - [User!]!	
Example
{
  "appearances": [Competitor],
  "createdAt": ISO8601Date,
  "dob": ISO8601Date,
  "entries": [AthleteEntry],
  "entriesWithPendingPayments": [Entry],
  "eventDivisions": [EventDivision],
  "id": "4",
  "image": "xyz789",
  "memberships": [AthleteMembership],
  "name": "abc123",
  "nationality": "xyz789",
  "physicalTags": [PhysicalTag],
  "properties": {},
  "ranks": [EventDivisionRank],
  "unfinishedEvents": [Event],
  "updatedAt": ISO8601Date,
  "users": [User]
}
Types
AthleteEntry
Fields
Field Name	Description
athlete - Athlete!	
athleteId - ID!	
bib - String	
eventDivision - EventDivision!	
eventDivisionId - ID!	
id - ID!	
rank - Int	
seed - Int	
status - EntryStatusEnum!	
teamMembers - [TeamMember!]	
teamName - String	
Example
{
  "athlete": Athlete,
  "athleteId": 4,
  "bib": "xyz789",
  "eventDivision": EventDivision,
  "eventDivisionId": 4,
  "id": 4,
  "rank": 987,
  "seed": 123,
  "status": "confirmed",
  "teamMembers": [TeamMember],
  "teamName": "xyz789"
}
Types
AthleteHeatInput
Description
Arguments for updating an athlete heat

Fields
Input Field	Description
heatId - ID!	
athleteId - ID	
athleteName - String	
position - Int!	
physicalTagId - String	
Example
{
  "heatId": "4",
  "athleteId": 4,
  "athleteName": "xyz789",
  "position": 123,
  "physicalTagId": "xyz789"
}
Types
AthleteInput
Description
Arguments for updating an athlete

Fields
Input Field	Description
name - String	
dob - String	
image - String	
userIds - [ID!]	
properties - JSON	
Example
{
  "name": "abc123",
  "dob": "xyz789",
  "image": "xyz789",
  "userIds": ["4"],
  "properties": {}
}
Types
AthleteMembership
Fields
Field Name	Description
athlete - Athlete!	
createdAt - ISO8601DateTime!	
divisions - [Division!]	
expired - Boolean!	
expiryDate - ISO8601Date	
id - ID!	
organisation - Organisation	
payments - [Payment!]	
properties - JSON	
series - Series	
Example
{
  "athlete": Athlete,
  "createdAt": ISO8601DateTime,
  "divisions": [Division],
  "expired": false,
  "expiryDate": ISO8601Date,
  "id": 4,
  "organisation": Organisation,
  "payments": [Payment],
  "properties": {},
  "series": Series
}
Types
AthleteRankingResult
Fields
Field Name	Description
athlete - Athlete!	
displayProperty - String	
eligibleResults - Int	
eventsToCount - [ID!]	
points - Int!	
results - [Result!]!	
resultsToCount - Int	
Example
{
  "athlete": Athlete,
  "displayProperty": "abc123",
  "eligibleResults": 987,
  "eventsToCount": [4],
  "points": 987,
  "results": [Result],
  "resultsToCount": 123
}
Types
BigInt
Description
Represents non-fractional signed whole numeric values. Since the value may exceed the size of a 32-bit integer, it's encoded as a string.

Example
{}
Types
Boolean
Description
Represents true or false values.

Types
Break
Fields
Field Name	Description
date - ISO8601DateTime!	
position - Int!	
Example
{"date": ISO8601DateTime, "position": 123}
Types
CancelEntryInput
Description
Autogenerated input type of CancelEntry

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
entryId - ID!	
Example
{
  "clientMutationId": "xyz789",
  "entryId": "4"
}
Types
CancelEntryPayload
Description
Autogenerated return type of CancelEntry.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
entry - Entry!	
Example
{
  "clientMutationId": "xyz789",
  "entry": Entry
}
Types
Competitor
Fields
Field Name	Description
athlete - Athlete!	
athleteId - ID!	
bib - String	
heat - Heat!	
heatId - ID!	
id - ID!	
position - Int!	
priority - Int	
result - HeatResult	
roundResult - HeatResult	
teamMembers - [TeamMember!]	
teamName - String	
Example
{
  "athlete": Athlete,
  "athleteId": 4,
  "bib": "abc123",
  "heat": Heat,
  "heatId": "4",
  "id": "4",
  "position": 987,
  "priority": 123,
  "result": HeatResult,
  "roundResult": HeatResult,
  "teamMembers": [TeamMember],
  "teamName": "abc123"
}
Types
CompetitorResult
Types
Union Types
Competitor

Entry

Example
Competitor
Types
Contest
Fields
Field Name	Description
config - ContestConfig!	
id - ID!	
name - String	
parent - Contest	
result - [ContestResult!]!	
savedConfig - ContestConfig!	
type - String!	
Example
{
  "config": ContestConfig,
  "id": "4",
  "name": "xyz789",
  "parent": Contest,
  "result": [PointsPerPlaceResult],
  "savedConfig": ContestConfig,
  "type": "abc123"
}
Types
ContestConfig
Fields
Field Name	Description
produces - ContestConfig	
result - ContestResultConfig	
shape - ContestShapeConfig	
Example
{
  "produces": ContestConfig,
  "result": ContestResultConfig,
  "shape": ContestShapeConfig
}
Types
ContestConfigInput
Fields
Input Field	Description
shape - ContestShapeConfigInput	
result - ContestResultConfigInput	
produces - ContestConfigInput	
Example
{
  "shape": ContestShapeConfigInput,
  "result": ContestResultConfigInput,
  "produces": ContestConfigInput
}
Types
ContestInput
Fields
Input Field	Description
id - ID!	
name - String	
config - ContestConfigInput!	
Example
{
  "id": 4,
  "name": "xyz789",
  "config": ContestConfigInput
}
Types
ContestProgressionConfig
Fields
Field Name	Description
max - Int	
toSibling - Int	
Example
{"max": 123, "toSibling": 987}
Types
ContestProgressionConfigInput
Fields
Input Field	Description
max - Int	
toSibling - Int	
Example
{"max": 123, "toSibling": 123}
Types
ContestResult
Types
Union Types
PointsPerPlaceResult

Example
PointsPerPlaceResult
Types
ContestResultConfig
Fields
Field Name	Description
config - ContestResultConfigConfig	
type - String!	
Example
{
  "config": ContestResultConfigConfig,
  "type": "abc123"
}
Types
ContestResultConfigConfig
Fields
Field Name	Description
pointsPerPlace - [Int!]	
Example
{"pointsPerPlace": [123]}
Types
ContestResultConfigConfigInput
Fields
Input Field	Description
pointsPerPlace - [Int!]	
Example
{"pointsPerPlace": [987]}
Types
ContestResultConfigInput
Fields
Input Field	Description
type - String	
config - ContestResultConfigConfigInput	
Example
{
  "type": "abc123",
  "config": ContestResultConfigConfigInput
}
Types
ContestShapeConfig
Fields
Field Name	Description
contestantsPerChild - Int	
heatDurationMinutes - Int	
numberOfChildren - Int	
progression - [ContestProgressionConfig!]	
Example
{
  "contestantsPerChild": 987,
  "heatDurationMinutes": 123,
  "numberOfChildren": 123,
  "progression": [ContestProgressionConfig]
}
Types
ContestShapeConfigInput
Fields
Input Field	Description
numberOfChildren - Int	
heatDurationMinutes - Int	
contestantsPerChild - Int	
progression - [ContestProgressionConfigInput!]	
Example
{
  "numberOfChildren": 123,
  "heatDurationMinutes": 123,
  "contestantsPerChild": 987,
  "progression": [ContestProgressionConfigInput]
}
Types
CopyEventInput
Description
Autogenerated input type of CopyEvent

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
event - EventInput!	
eventId - ID!	
Example
{
  "clientMutationId": "abc123",
  "event": EventInput,
  "eventId": "4"
}
Types
CopyEventPayload
Description
Autogenerated return type of CopyEvent.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
event - Event	
Example
{
  "clientMutationId": "abc123",
  "event": Event
}
Types
CreateEntriesInput
Description
Autogenerated input type of CreateEntries

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventId - ID!	
entries - [EntryInput!]!	
Example
{
  "clientMutationId": "xyz789",
  "eventId": "4",
  "entries": [EntryInput]
}
Types
CreateEntriesPayload
Description
Autogenerated return type of CreateEntries.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
entries - [Entry!]!	
Example
{
  "clientMutationId": "xyz789",
  "entries": [Entry]
}
Types
CreateEventInput
Description
Autogenerated input type of CreateEvent

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
event - EventInput!	
Example
{
  "clientMutationId": "xyz789",
  "event": EventInput
}
Types
CreateEventPayload
Description
Autogenerated return type of CreateEvent.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
event - Event	
Example
{
  "clientMutationId": "abc123",
  "event": Event
}
Types
CreateMembershipInput
Description
Autogenerated input type of CreateMembership

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
membership - MembershipInput!	
Example
{
  "clientMutationId": "abc123",
  "membership": MembershipInput
}
Types
CreateMembershipPayload
Description
Autogenerated return type of CreateMembership.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
membership - Membership	
Example
{
  "clientMutationId": "abc123",
  "membership": Membership
}
Types
CreateOrganisationInput
Description
Autogenerated input type of CreateOrganisation

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
organisation - OrganisationInput!	
Example
{
  "clientMutationId": "abc123",
  "organisation": OrganisationInput
}
Types
CreateOrganisationPayload
Description
Autogenerated return type of CreateOrganisation.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
organisation - Organisation!	
Example
{
  "clientMutationId": "xyz789",
  "organisation": Organisation
}
Types
CreateOrganisationPropertyInput
Description
Autogenerated input type of CreateOrganisationProperty

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
property - PropertyInput!	
Example
{
  "clientMutationId": "xyz789",
  "id": "4",
  "property": PropertyInput
}
Types
CreateOrganisationPropertyPayload
Description
Autogenerated return type of CreateOrganisationProperty.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
property - Property!	
Example
{
  "clientMutationId": "abc123",
  "property": Property
}
Types
CreditBaselinePrice
Fields
Field Name	Description
price - Int!	
size - String!	
Example
{"price": 123, "size": "xyz789"}
Types
CustomFieldsRegistrationInput
Description
Arguments for capture fields

Fields
Input Field	Description
uuid - ID!	
required - Boolean	
config - PropertyConfigInput	
Example
{
  "uuid": 4,
  "required": false,
  "config": PropertyConfigInput
}
Types
CutLine
Fields
Field Name	Description
description - String!	
divisionId - ID!	
position - Int!	
Example
{
  "description": "abc123",
  "divisionId": "4",
  "position": 987
}
Types
DeleteContestInput
Description
Autogenerated input type of DeleteContest

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
Example
{
  "clientMutationId": "xyz789",
  "id": "4"
}
Types
DeleteContestPayload
Description
Autogenerated return type of DeleteContest.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivision - EventDivision!	
Example
{
  "clientMutationId": "abc123",
  "eventDivision": EventDivision
}
Types
DeleteHeatInput
Description
Autogenerated input type of DeleteHeat

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
Example
{"clientMutationId": "abc123", "id": 4}
Types
DeleteHeatPayload
Description
Autogenerated return type of DeleteHeat.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivision - EventDivision!	
heat - Heat!	
Example
{
  "clientMutationId": "xyz789",
  "eventDivision": EventDivision,
  "heat": Heat
}
Types
DeleteMembershipInput
Description
Autogenerated input type of DeleteMembership

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
Example
{
  "clientMutationId": "abc123",
  "id": "4"
}
Types
DeleteMembershipPayload
Description
Autogenerated return type of DeleteMembership.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
membership - Membership!	
Example
{
  "clientMutationId": "xyz789",
  "membership": Membership
}
Types
DeleteRankingRuleOverrideInput
Description
Autogenerated input type of DeleteRankingRuleOverride

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
Example
{"clientMutationId": "xyz789", "id": 4}
Types
DeleteRankingRuleOverridePayload
Description
Autogenerated return type of DeleteRankingRuleOverride.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
rankingRuleOverride - RankingRuleOverride!	
Example
{
  "clientMutationId": "abc123",
  "rankingRuleOverride": RankingRuleOverride
}
Types
DeleteSeriesInput
Description
Autogenerated input type of DeleteSeries

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
Example
{"clientMutationId": "xyz789", "id": 4}
Types
DeleteSeriesPayload
Description
Autogenerated return type of DeleteSeries.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
series - Series!	
Example
{
  "clientMutationId": "xyz789",
  "series": Series
}
Types
Division
Fields
Field Name	Description
id - ID!	
name - String!	
restrictions - [Restriction!]	
Example
{
  "id": "4",
  "name": "abc123",
  "restrictions": [Restriction]
}
Types
DivisionInput
Description
Arguments for creating or updating a division

Fields
Input Field	Description
id - ID	
uuid - String	
name - String	
organisationId - ID	When this argument is set, this division will be saved within the organisations's default divisions
Example
{
  "id": "4",
  "uuid": "abc123",
  "name": "abc123",
  "organisationId": 4
}
Types
DivisionToSeasons
Fields
Field Name	Description
divisionId - ID!	
id - ID!	
pointAllocation - PointAllocation	
pointAllocationId - ID	
seasonId - ID!	
Example
{
  "divisionId": 4,
  "id": "4",
  "pointAllocation": PointAllocation,
  "pointAllocationId": "4",
  "seasonId": 4
}
Types
EditOrganisationInput
Description
Arguments for updating an organisation

Fields
Input Field	Description
id - ID!	
name - String	
sportType - SportType	
shortName - String	
contactEmail - String	
docusealApiKey - String	
docusealAdminEmail - String	
facebook - String	
instagram - String	
logo - String	
Example
{
  "id": "4",
  "name": "abc123",
  "sportType": "surf",
  "shortName": "abc123",
  "contactEmail": "abc123",
  "docusealApiKey": "xyz789",
  "docusealAdminEmail": "xyz789",
  "facebook": "abc123",
  "instagram": "xyz789",
  "logo": "xyz789"
}
Types
Email
Fields
Field Name	Description
body - String	
createdAt - ISO8601DateTime!	
eventId - ID!	
subject - String	
Example
{
  "body": "abc123",
  "createdAt": ISO8601DateTime,
  "eventId": "4",
  "subject": "xyz789"
}
Types
Entry
Fields
Field Name	Description
athlete - Athlete!	
athleteId - ID!	
bib - String	
eventDivision - EventDivision!	
eventDivisionId - ID!	
id - ID!	
rank - Int	
seed - Int	
status - EntryStatusEnum!	
teamMembers - [TeamMember!]	
teamName - String	
Example
{
  "athlete": Athlete,
  "athleteId": "4",
  "bib": "xyz789",
  "eventDivision": EventDivision,
  "eventDivisionId": 4,
  "id": 4,
  "rank": 123,
  "seed": 123,
  "status": "confirmed",
  "teamMembers": [TeamMember],
  "teamName": "xyz789"
}
Types
EntryAthleteInput
Description
Arguments for creating or using an existing athlete when creating an entry or when adding an athlete to a team entry in a teams contest

Fields
Input Field	Description
id - ID	
name - String!	
dob - ISO8601DateTime	
properties - JSON	
Example
{
  "id": 4,
  "name": "xyz789",
  "dob": ISO8601DateTime,
  "properties": {}
}
Types
EntryInput
Description
Arguments for creating an entry in a specific event division. If the athleteId is specified, it will create the entry for the specific athlete. When the athleteId is not specified, it will try to use an existing federation athlete with the same name supplied inside the athlete input, and if none find will create a new athlete

Fields
Input Field	Description
eventDivisionId - ID!	
athleteId - ID	
athlete - EntryAthleteInput!	
teamMembers - [EntryTeamMemberInput!]	
teamName - String	
bib - String	
seed - Int	If the seed is not provided, the system will use the current rankings seed, if any
properties - JSON	
Example
{
  "eventDivisionId": 4,
  "athleteId": "4",
  "athlete": EntryAthleteInput,
  "teamMembers": [EntryTeamMemberInput],
  "teamName": "abc123",
  "bib": "abc123",
  "seed": 123,
  "properties": {}
}
Types
EntryLimit
Fields
Field Name	Description
id - ID!	
limit - Int!	
Example
{"id": 4, "limit": 987}
Types
EntryLimitInput
Fields
Input Field	Description
id - ID	
limit - Int	
Example
{"id": "4", "limit": 987}
Types
EntryStatusEnum
Values
Enum Value	Description
confirmed

waitlisted

denied

Example
"confirmed"
Types
EntryTeamMemberInput
Description
Arguments for creating team members for a team competing in a relays or teams type contest.

Fields
Input Field	Description
order - Int!	
athleteId - ID	
teamRoleId - ID	
athlete - EntryAthleteInput!	
Example
{
  "order": 987,
  "athleteId": "4",
  "teamRoleId": "4",
  "athlete": EntryAthleteInput
}
Types
Event
Fields
Field Name	Description
activeEntriesUsers - [User!]!	
captureFields - [Property!]!	
config - EventConfig	
currentHeats - [Heat]!	
currentScheduleIndex - Int!	
date - ISO8601DateTime!	
daysWindow - Int!	
eventDivisions - [EventDivision!]	
fullSchedule - Schedule!	
hideEntries - Boolean!	
hideFinals - Boolean	
hideScheduledTime - Boolean!	
id - ID!	
location - Location	
name - String!	
organisation - Organisation!	
organisationId - ID!	
paymentOptions - PaymentOptions	
priorityEnabled - Boolean	
registrationOptions - RegistrationOptions	
seedFromSeriesId - ID	
sentEmails - [Email!]	
series - [Series!]!	
status - EventStatus!	
teamLeaderboard - EventTeamLeaderboard	
teams - [Team!]!	
youtubeVideoId - String	
Example
{
  "activeEntriesUsers": [User],
  "captureFields": [Property],
  "config": EventConfig,
  "currentHeats": [Heat],
  "currentScheduleIndex": 123,
  "date": ISO8601DateTime,
  "daysWindow": 123,
  "eventDivisions": [EventDivision],
  "fullSchedule": Schedule,
  "hideEntries": true,
  "hideFinals": true,
  "hideScheduledTime": false,
  "id": "4",
  "location": Location,
  "name": "abc123",
  "organisation": Organisation,
  "organisationId": "4",
  "paymentOptions": PaymentOptions,
  "priorityEnabled": false,
  "registrationOptions": RegistrationOptions,
  "seedFromSeriesId": "4",
  "sentEmails": [Email],
  "series": [Series],
  "status": "scheduled",
  "teamLeaderboard": EventTeamLeaderboard,
  "teams": [Team],
  "youtubeVideoId": "abc123"
}
Types
EventAddOnsPurchase
Fields
Field Name	Description
broadcast - Int	
fisExport - Int	
priority - Int	
Example
{"broadcast": 123, "fisExport": 123, "priority": 123}
Types
EventConfig
Fields
Field Name	Description
disableSchedule - Boolean	
teamLeaderboard - EventTeamLeaderboardConfig	
Example
{
  "disableSchedule": true,
  "teamLeaderboard": EventTeamLeaderboardConfig
}
Types
EventConfigInput
Fields
Input Field	Description
teamLeaderboard - EventTeamLeaderboardConfigInput	
Example
{"teamLeaderboard": EventTeamLeaderboardConfigInput}
Types
EventCreditsPurchase
Fields
Field Name	Description
l - Int	
m - Int	
s - Int	
unlimited - Int	
xl - Int	
xs - Int	
Example
{"l": 123, "m": 123, "s": 987, "unlimited": 123, "xl": 123, "xs": 123}
Types
EventDivision
Fields
Field Name	Description
contestId - ID	
defaultEventDurationMinutes - Int!	
division - Division!	
divisionToSeasons - [DivisionToSeasons!]	
entries - [Entry!]!	
entryCount - Int!	
entryLimit - EntryLimit	
event - Event!	
eventDivision - EventDivision	
eventDivisionId - ID	
eventDivisionPointAllocations - [EventDivisionPointAllocations!]	
eventDivisions - [EventDivision!]!	
formatDefinition - FormatDefinition	
heatConfig - HeatConfig	
heatDurationMinutes - Int	
heats - [Heat!]!	
id - ID!	
leaderboards - [Leaderboard!]	
Arguments
round - Int
order - Int	
previewDraw - PreviewDraw!	
Arguments
formatDefinition - FormatDefinitionInput!
entryLimit - EntryLimitInput
properties - JSON	
ranking - [EventDivisionRank!]	
Arguments
eventDivisionId - ID
seededRounds - [SeededRound!]	
status - EventDivisionStatus!	
teamLeaderboard - EventDivisionTeamLeaderboard	
template - Template!	
Example
{
  "contestId": 4,
  "defaultEventDurationMinutes": 123,
  "division": Division,
  "divisionToSeasons": [DivisionToSeasons],
  "entries": [Entry],
  "entryCount": 987,
  "entryLimit": EntryLimit,
  "event": Event,
  "eventDivision": EventDivision,
  "eventDivisionId": "4",
  "eventDivisionPointAllocations": [
    EventDivisionPointAllocations
  ],
  "eventDivisions": [EventDivision],
  "formatDefinition": FormatDefinition,
  "heatConfig": HeatConfig,
  "heatDurationMinutes": 987,
  "heats": [Heat],
  "id": "4",
  "leaderboards": [Leaderboard],
  "order": 987,
  "previewDraw": PreviewDraw,
  "properties": {},
  "ranking": [EventDivisionRank],
  "seededRounds": [SeededRound],
  "status": "registration_open",
  "teamLeaderboard": EventDivisionTeamLeaderboard,
  "template": Template
}
Types
EventDivisionInput
Description
Arguments for creating or updating an event division

Fields
Input Field	Description
id - ID	
templateId - ID	Set the competition template to use in this event division. If this value is not set, the event division will be created with the organisation's default template.
order - Int	Set the order so that event divisions are listed in order within the event
divisionId - ID	Pass a divisionId when using an existing division
division - DivisionInput	Pass a division object when creating a new division
entryLimit - EntryLimitInput	Pass an entryLimit object when limiting the available spots in a division
Example
{
  "id": 4,
  "templateId": 4,
  "order": 987,
  "divisionId": "4",
  "division": DivisionInput,
  "entryLimit": EntryLimitInput
}
Types
EventDivisionPointAllocations
Fields
Field Name	Description
eventDivisionId - ID!	
id - ID!	
pointAllocation - PointAllocation	
pointAllocationId - ID	
seasonId - ID!	
Example
{
  "eventDivisionId": "4",
  "id": 4,
  "pointAllocation": PointAllocation,
  "pointAllocationId": 4,
  "seasonId": "4"
}
Types
EventDivisionRank
Fields
Field Name	Description
athleteId - ID	
competitor - Competitor!	
eventDivisionId - ID!	
excluded - Boolean	
id - ID!	
place - BigInt	
rides - JSON	
total - Float!	
Example
{
  "athleteId": "4",
  "competitor": Competitor,
  "eventDivisionId": "4",
  "excluded": true,
  "id": 4,
  "place": {},
  "rides": {},
  "total": 123.45
}
Types
EventDivisionStatus
Values
Enum Value	Description
registration_open

registration_closed

drawn

Example
"registration_open"
Types
EventDivisionTeamLeaderboard
Fields
Field Name	Description
id - ID!	
result - [EventDivisionTeamLeaderboardResult!]!	
Example
{
  "id": "4",
  "result": [EventDivisionTeamLeaderboardResult]
}
Types
EventDivisionTeamLeaderboardResult
Fields
Field Name	Description
memberResults - [HeatResult!]!	
place - Int	
teamName - String!	
total - Float	
Example
{
  "memberResults": [HeatResult],
  "place": 123,
  "teamName": "xyz789",
  "total": 987.65
}
Types
EventInput
Description
Arguments for creating or updating an event

Fields
Input Field	Description
id - ID	
status - EventStatus	
name - String!	
organisationId - ID!	
date - ISO8601DateTime!	
daysWindow - Int!	
seriesIds - [ID!]	
seedFromSeriesId - ID	
eventDivisions - [EventDivisionInput!]!	
customFieldsRegistrationsAttributes - [CustomFieldsRegistrationInput!]	
location - LocationInput	
Example
{
  "id": 4,
  "status": "scheduled",
  "name": "abc123",
  "organisationId": 4,
  "date": ISO8601DateTime,
  "daysWindow": 123,
  "seriesIds": [4],
  "seedFromSeriesId": 4,
  "eventDivisions": [EventDivisionInput],
  "customFieldsRegistrationsAttributes": [
    CustomFieldsRegistrationInput
  ],
  "location": LocationInput
}
Types
EventStatus
Values
Enum Value	Description
scheduled

upcoming

drawn

published

on

on_hold

finished

results_published

cancelled

Example
"scheduled"
Types
EventTeamLeaderboard
Fields
Field Name	Description
config - EventTeamLeaderboardConfig	
id - ID!	
result - [EventTeamLeaderboardResult!]!	
Example
{
  "config": EventTeamLeaderboardConfig,
  "id": "4",
  "result": [EventTeamLeaderboardResult]
}
Types
EventTeamLeaderboardConfig
Fields
Field Name	Description
pointsPerPlace - [Int]	
Example
{"pointsPerPlace": [123]}
Types
EventTeamLeaderboardConfigInput
Fields
Input Field	Description
pointsPerPlace - [Int!]!	
Example
{"pointsPerPlace": [123]}
Types
EventTeamLeaderboardResult
Fields
Field Name	Description
place - Int!	
placeCounts - [Int]!	
teamName - String!	
total - Float!	
Example
{
  "place": 123,
  "placeCounts": [987],
  "teamName": "xyz789",
  "total": 987.65
}
Types
ExcludeAthleteFromRankingsInput
Description
Autogenerated input type of ExcludeAthleteFromRankings

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivisionId - ID!	
childEventDivisionId - ID	
athleteId - ID!	
exclude - Boolean!	
Example
{
  "clientMutationId": "xyz789",
  "eventDivisionId": 4,
  "childEventDivisionId": "4",
  "athleteId": 4,
  "exclude": false
}
Types
ExcludeAthleteFromRankingsPayload
Description
Autogenerated return type of ExcludeAthleteFromRankings.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivision - EventDivision!	
Example
{
  "clientMutationId": "xyz789",
  "eventDivision": EventDivision
}
Types
Extras
Fields
Field Name	Description
name - String!	
size - String	
uuid - String	
Example
{
  "name": "xyz789",
  "size": "abc123",
  "uuid": "xyz789"
}
Types
FederationRootEnum
Values
Enum Value	Description
root

self

Example
"root"
Types
FederationTeams
Fields
Field Name	Description
teams - [Team!]!	
totalCount - Int!	
Example
{"teams": [Team], "totalCount": 987}
Types
Float
Description
Represents signed double-precision fractional values as specified by IEEE 754.

Example
987.65
Types
FormatDefinition
Fields
Field Name	Description
defaultHeatDurationMinutes - Int	
entriesRandomized - Boolean	
hasBibs - Boolean	
heatSizes - JSON	
hideSeeds - Boolean	
isTeams - Boolean	
manualProgression - JSON	
numberOfRounds - Int	
progression - JSON	
roundBased - Boolean	
runBased - Boolean	
runProgression - JSON	
seeds - JSON	
teamConfig - TeamConfig	
teamLeaderboard - Boolean!	
Example
{
  "defaultHeatDurationMinutes": 123,
  "entriesRandomized": true,
  "hasBibs": true,
  "heatSizes": {},
  "hideSeeds": false,
  "isTeams": false,
  "manualProgression": {},
  "numberOfRounds": 123,
  "progression": {},
  "roundBased": true,
  "runBased": true,
  "runProgression": {},
  "seeds": {},
  "teamConfig": TeamConfig,
  "teamLeaderboard": true
}
Types
FormatDefinitionInput
Description
Arguments for updating format definition

Fields
Input Field	Description
numberOfRounds - Int	
roundBased - Boolean	
runBased - Boolean	
teamLeaderboard - Boolean	
isTeams - Boolean	
teamConfig - TeamConfigInput	
seeds - JSON	
manualProgression - JSON	
heatSizes - JSON	
progression - JSON	
runProgression - JSON	
defaultHeatDurationMinutes - Int	
hideSeeds - Boolean	
hasBibs - Boolean	
entriesRandomized - Boolean	
Example
{
  "numberOfRounds": 123,
  "roundBased": false,
  "runBased": false,
  "teamLeaderboard": false,
  "isTeams": false,
  "teamConfig": TeamConfigInput,
  "seeds": {},
  "manualProgression": {},
  "heatSizes": {},
  "progression": {},
  "runProgression": {},
  "defaultHeatDurationMinutes": 987,
  "hideSeeds": false,
  "hasBibs": false,
  "entriesRandomized": false
}
Types
Heat
Fields
Field Name	Description
competitors - [Competitor!]!	
config - HeatConfig!	
contestId - ID	
endTime - ISO8601DateTime	
eventDivision - EventDivision!	
eventDivisionId - ID!	
group - HeatGroup	
heatDurationMinutes - Int	
id - ID!	
podium - String	
position - Int!	
progressions - [HeatProgression]	
result - [HeatResult!]!	
round - String!	
roundPosition - Int!	
scheduledTime - ISO8601DateTime	
Arguments
recalculate - Boolean
startTime - ISO8601DateTime	
Example
{
  "competitors": [Competitor],
  "config": HeatConfig,
  "contestId": "4",
  "endTime": ISO8601DateTime,
  "eventDivision": EventDivision,
  "eventDivisionId": "4",
  "group": HeatGroup,
  "heatDurationMinutes": 987,
  "id": 4,
  "podium": "abc123",
  "position": 987,
  "progressions": [HeatProgression],
  "result": [HeatResult],
  "round": "abc123",
  "roundPosition": 123,
  "scheduledTime": ISO8601DateTime,
  "startTime": ISO8601DateTime
}
Types
HeatConfig
Fields
Field Name	Description
athleteRidesLimit - Int	
calculator - String	
categories - JSON	
hasLeaderboard - Boolean	
hasPriority - Boolean	
hasStartlist - Boolean	
heatSize - Int!	
hideNeeds - Boolean	
hideScheduledTime - Boolean	
hideScores - Boolean	
hideTimer - Boolean	
inputFormat - String	
isTeams - Boolean	
jerseyOrder - [String!]	
maxRideScore - Int!	
numberOfLanes - Int	
runBased - Boolean	
teamConfig - TeamConfig	
totalCountingRides - Int	
usesLanes - Boolean	
Example
{
  "athleteRidesLimit": 987,
  "calculator": "abc123",
  "categories": {},
  "hasLeaderboard": true,
  "hasPriority": false,
  "hasStartlist": true,
  "heatSize": 123,
  "hideNeeds": true,
  "hideScheduledTime": true,
  "hideScores": true,
  "hideTimer": true,
  "inputFormat": "abc123",
  "isTeams": false,
  "jerseyOrder": ["xyz789"],
  "maxRideScore": 123,
  "numberOfLanes": 123,
  "runBased": false,
  "teamConfig": TeamConfig,
  "totalCountingRides": 987,
  "usesLanes": false
}
Types
HeatGroup
Fields
Field Name	Description
groupContestId - ID	
name - String	
roundContestId - ID	
roundName - String	
Example
{
  "groupContestId": "4",
  "name": "abc123",
  "roundContestId": "4",
  "roundName": "abc123"
}
Types
HeatProgression
Fields
Field Name	Description
heat - Int!	
obscure - Boolean	
position - Int!	
round - String!	
roundOnly - Boolean	
roundPosition - Int!	
run - Boolean	
Example
{
  "heat": 123,
  "obscure": true,
  "position": 987,
  "round": "xyz789",
  "roundOnly": false,
  "roundPosition": 123,
  "run": true
}
Types
HeatResult
Fields
Field Name	Description
athleteId - ID!	
competitor - Competitor!	
countingMember - Boolean	
needs - Float	
place - BigInt	
rides - JSON!	
total - Float!	
winBy - Float	
Example
{
  "athleteId": 4,
  "competitor": Competitor,
  "countingMember": true,
  "needs": 123.45,
  "place": {},
  "rides": {},
  "total": 123.45,
  "winBy": 987.65
}
Types
HierarchyLevelEnum
Values
Enum Value	Description
self_and_ancestors

descendants

Example
"self_and_ancestors"
Types
ID
Description
Represents a unique identifier that is Base64 obfuscated. It is often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as "VXNlci0xMA==") or integer (such as 4) input value will be accepted as an ID.

Example
4
Types
ISO8601Date
Description
An ISO 8601-encoded date

Example
ISO8601Date
Types
ISO8601DateTime
Description
An ISO 8601-encoded datetime

Example
ISO8601DateTime
Types
Int
Description
Represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

Example
123
Types
JSON
Description
Represents untyped JSON

Example
{}
Types
Leaderboard
Fields
Field Name	Description
competitors - [Competitor!]!	
config - HeatConfig!	
endTime - ISO8601DateTime	
eventDivision - EventDivision!	
heatDurationMinutes - Int	
heats - [Heat!]!	
id - ID!	
result - [HeatResult!]!	
round - String!	
roundPosition - Int!	
startTime - ISO8601DateTime	
Example
{
  "competitors": [Competitor],
  "config": HeatConfig,
  "endTime": ISO8601DateTime,
  "eventDivision": EventDivision,
  "heatDurationMinutes": 987,
  "heats": [Heat],
  "id": "4",
  "result": [HeatResult],
  "round": "abc123",
  "roundPosition": 123,
  "startTime": ISO8601DateTime
}
Types
LinkTagToAthleteInput
Description
Autogenerated input type of LinkTagToAthlete

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
serialNumber - ID!	
humanReadableId - ID	
athleteId - ID!	
Example
{
  "clientMutationId": "abc123",
  "serialNumber": "4",
  "humanReadableId": "4",
  "athleteId": "4"
}
Types
LinkTagToAthletePayload
Description
Autogenerated return type of LinkTagToAthlete.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
tag - PhysicalTag	
Example
{
  "clientMutationId": "abc123",
  "tag": PhysicalTag
}
Types
Location
Fields
Field Name	Description
formattedAddress - String!	
Example
{"formattedAddress": "xyz789"}
Types
LocationCoordinatesInput
Fields
Input Field	Description
lat - Float!	Latitude
lng - Float!	Longitude
Example
{"lat": 123.45, "lng": 987.65}
Types
LocationInput
Description
Arguments for event location

Fields
Input Field	Description
id - ID!	ID of location
formattedAddress - String!	A full human-readable address for this place
googleMapsUri - String!	Google Maps URI for this location
location - LocationCoordinatesInput!	Coordinates for this location
placePredictionText - String!	A human-readable name for this place
utcOffsetMinutes - Int!	UTC offset in minutes
Example
{
  "id": "4",
  "formattedAddress": "xyz789",
  "googleMapsUri": "xyz789",
  "location": LocationCoordinatesInput,
  "placePredictionText": "abc123",
  "utcOffsetMinutes": 123
}
Types
MarketFactor
Fields
Field Name	Description
currency - String!	
decimalMultiplier - Int!	
factor - Float!	
Example
{
  "currency": "abc123",
  "decimalMultiplier": 987,
  "factor": 987.65
}
Types
MemberAthleteInput
Description
arguments for creating or updating a member athlete.

Fields
Input Field	Description
id - ID	
name - String!	
dob - String	
user - UserInput!	
Example
{
  "id": "4",
  "name": "xyz789",
  "dob": "xyz789",
  "user": UserInput
}
Types
Membership
Fields
Field Name	Description
athlete - Athlete!	
createdAt - ISO8601DateTime!	
divisions - [Division!]	
expired - Boolean!	
expiryDate - ISO8601Date	
id - ID!	
organisation - Organisation	
payments - [Payment!]	
properties - JSON	
series - Series	
Example
{
  "athlete": Athlete,
  "createdAt": ISO8601DateTime,
  "divisions": [Division],
  "expired": true,
  "expiryDate": ISO8601Date,
  "id": 4,
  "organisation": Organisation,
  "payments": [Payment],
  "properties": {},
  "series": Series
}
Types
MembershipInput
Description
arguments for creating a membership.

Fields
Input Field	Description
id - ID	
organisationId - ID!	
seriesId - ID	
divisionIds - [ID!]	
expiryDate - String	
properties - JSON	
athlete - MemberAthleteInput	
Example
{
  "id": 4,
  "organisationId": 4,
  "seriesId": "4",
  "divisionIds": [4],
  "expiryDate": "xyz789",
  "properties": {},
  "athlete": MemberAthleteInput
}
Types
MembershipUpdateInput
Description
arguments for updating a membership.

Fields
Input Field	Description
id - ID	
organisationId - ID!	
seriesId - ID	
divisionIds - [ID!]	
expiryDate - String	
properties - JSON	
Example
{
  "id": "4",
  "organisationId": 4,
  "seriesId": "4",
  "divisionIds": [4],
  "expiryDate": "xyz789",
  "properties": {}
}
Types
Memberships
Fields
Field Name	Description
memberships - [Membership!]!	
totalCount - Int!	
Example
{"memberships": [Membership], "totalCount": 123}
Types
MergeAthletesInput
Description
Autogenerated input type of MergeAthletes

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
primary - ID!	
others - [ID!]!	
Example
{
  "clientMutationId": "xyz789",
  "primary": "4",
  "others": ["4"]
}
Types
MergeAthletesPayload
Description
Autogenerated return type of MergeAthletes.

Fields
Field Name	Description
athlete - Athlete!	
clientMutationId - String	A unique identifier for the client performing the mutation.
Example
{
  "athlete": Athlete,
  "clientMutationId": "abc123"
}
Types
MoveHeatItemInput
Description
Arguments for moving heat items

Fields
Input Field	Description
type - MoveHeatItemTypeEnum!	
heatId - ID!	
position - Int!	
removedItems - [Int!]	
data - MoveHeatItemProgressionInput	
Example
{
  "type": "competitor",
  "heatId": "4",
  "position": 123,
  "removedItems": [123],
  "data": MoveHeatItemProgressionInput
}
Types
MoveHeatItemProgressionInput
Description
Arguments for progression

Fields
Input Field	Description
heat - Int!	
position - Int!	
roundPosition - Int!	
Example
{"heat": 987, "position": 123, "roundPosition": 123}
Types
MoveHeatItemTypeEnum
Values
Enum Value	Description
competitor

progression

empty

Example
"competitor"
Types
MoveHeatItemsInput
Description
Autogenerated input type of MoveHeatItems

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivisionId - ID!	
source - MoveHeatItemInput!	
target - MoveHeatItemInput!	
Example
{
  "clientMutationId": "abc123",
  "eventDivisionId": "4",
  "source": MoveHeatItemInput,
  "target": MoveHeatItemInput
}
Types
MoveHeatItemsPayload
Description
Autogenerated return type of MoveHeatItems.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heats - [Heat!]!	
Example
{
  "clientMutationId": "xyz789",
  "heats": [Heat]
}
Types
Options
Fields
Field Name	Description
currency - String	
defaultDivisionPrice - Int	
divisions - [PaymentOptionsDivisions!]	
extraDivisionPrice - Int	
extras - [PaymentExtra!]	
familyTotal - JSON	
federatedMembership - Boolean	
managedByParent - Boolean	
rollingMembership - RollingMembership	
Example
{
  "currency": "abc123",
  "defaultDivisionPrice": 123,
  "divisions": [PaymentOptionsDivisions],
  "extraDivisionPrice": 987,
  "extras": [PaymentExtra],
  "familyTotal": {},
  "federatedMembership": false,
  "managedByParent": false,
  "rollingMembership": RollingMembership
}
Types
Organisation
Fields
Field Name	Description
activePurchases - ActivePurchases	
contactEmail - String!	
customProperties - [Property!]	
Arguments
levels - [PropertyLevelEnum!]!
divisions - [Division!]!	
docusealEnabled - Boolean!	
events - [Event!]!	
facebook - String	
federatedOrganisationTerm - String	
federatedOrganisations - [Organisation!]	
federationPointAllocations - [PointAllocation!]!	
federationProperties - [Property!]!	
Arguments
levels - [PropertyLevelEnum!]!
federationSeries - [Series!]!	
Arguments
hierarchy - HierarchyLevelEnum
federationTeams - [Team!]!	
Arguments
root - FederationRootEnum!
federationTemplates - [Template!]!	
id - ID!	
instagram - String	
latestPayment - Payment	
logo - String	Image URL with an implicit max-width. Accepts any number > 0 for size in pixels or "original" for the original image
Arguments
size - StringOrInteger
name - String!	
payables - [Payable!]	
paymentsEnabled - Boolean!	
paymentsReceived - Payments	
Arguments
payableId - ID
payableType - String
page - Int!
per - Int!
series - [Series!]!	
shortName - String!	
sportType - String!	
stripeAccountDetails - StripeAccountDetails!	
transactionFee - Float!	
useNfc - Boolean	
Example
{
  "activePurchases": ActivePurchases,
  "contactEmail": "abc123",
  "customProperties": [Property],
  "divisions": [Division],
  "docusealEnabled": false,
  "events": [Event],
  "facebook": "xyz789",
  "federatedOrganisationTerm": "xyz789",
  "federatedOrganisations": [Organisation],
  "federationPointAllocations": [PointAllocation],
  "federationProperties": [Property],
  "federationSeries": [Series],
  "federationTeams": [Team],
  "federationTemplates": [Template],
  "id": 4,
  "instagram": "xyz789",
  "latestPayment": Payment,
  "logo": "xyz789",
  "name": "xyz789",
  "payables": [Event],
  "paymentsEnabled": true,
  "paymentsReceived": Payments,
  "series": [Series],
  "shortName": "xyz789",
  "sportType": "xyz789",
  "stripeAccountDetails": StripeAccountDetails,
  "transactionFee": 123.45,
  "useNfc": false
}
Types
OrganisationAthletes
Fields
Field Name	Description
athletes - [Athlete!]!	
totalCount - Int!	
Example
{"athletes": [Athlete], "totalCount": 987}
Types
OrganisationInput
Description
Arguments for creating or updating an organisation

Fields
Input Field	Description
id - ID	
name - String!	
sportType - SportType!	
shortName - String!	
contactEmail - String!	
facebook - String	
instagram - String	
logo - String	
Example
{
  "id": "4",
  "name": "abc123",
  "sportType": "surf",
  "shortName": "abc123",
  "contactEmail": "xyz789",
  "facebook": "abc123",
  "instagram": "xyz789",
  "logo": "xyz789"
}
Types
OrganisationUserInput
Description
Arguments for creating an organisation user

Fields
Input Field	Description
name - String!	
email - String!	
role - UserRole!	
organisationId - ID!	
Example
{
  "name": "abc123",
  "email": "xyz789",
  "role": "director",
  "organisationId": 4
}
Types
Owner
Types
Union Types
User

Example
User
Types
Parameter
Fields
Field Name	Description
name - String!	
path - String!	
Example
{
  "name": "abc123",
  "path": "abc123"
}
Types
Payable
Types
Union Types
Event

Series

Example
Event
Types
Payment
Fields
Field Name	Description
amount - Int!	
chargeId - String	
createdAt - ISO8601DateTime!	
currency - String!	
directCharge - Boolean!	
entries - [Entry!]!	
fee - Int!	
id - ID!	
intentId - String	
payable - Payable!	
purchasedOptions - PurchasedOptions	
refunds - [Refund!]	
registrationError - String	
status - String!	
user - User!	
Example
{
  "amount": 987,
  "chargeId": "xyz789",
  "createdAt": ISO8601DateTime,
  "currency": "xyz789",
  "directCharge": true,
  "entries": [Entry],
  "fee": 123,
  "id": "4",
  "intentId": "xyz789",
  "payable": Event,
  "purchasedOptions": PurchasedOptions,
  "refunds": [Refund],
  "registrationError": "xyz789",
  "status": "abc123",
  "user": User
}
Types
PaymentExtra
Fields
Field Name	Description
name - String!	
options - [String!]	
price - Int!	
uuid - String!	
Example
{
  "name": "abc123",
  "options": ["abc123"],
  "price": 123,
  "uuid": "abc123"
}
Types
PaymentOptions
Fields
Field Name	Description
currency - String	
defaultDivisionPrice - Int	
divisions - [PaymentOptionsDivisions!]	
extraDivisionPrice - Int	
extras - [PaymentExtra!]	
familyTotal - JSON	
Example
{
  "currency": "abc123",
  "defaultDivisionPrice": 987,
  "divisions": [PaymentOptionsDivisions],
  "extraDivisionPrice": 123,
  "extras": [PaymentExtra],
  "familyTotal": {}
}
Types
PaymentOptionsDivisions
Fields
Field Name	Description
id - ID	
price - Int	
Example
{"id": 4, "price": 987}
Types
Payments
Fields
Field Name	Description
payments - [Payment!]!	
totalCount - Int!	
Example
{"payments": [Payment], "totalCount": 123}
Types
Permission
Fields
Field Name	Description
id - ID!	
owner - Owner!	
Example
{
  "id": "4",
  "owner": User
}
Types
PermissionInput
Description
Records for creating a permission

Fields
Input Field	Description
owner - UserInput!	
record - RecordInput!	
scopes - String!	
Example
{
  "owner": UserInput,
  "record": RecordInput,
  "scopes": "xyz789"
}
Types
PhysicalTag
Fields
Field Name	Description
athlete - Athlete	
athleteId - ID	
humanReadableId - ID	
id - ID!	
Example
{
  "athlete": Athlete,
  "athleteId": "4",
  "humanReadableId": "4",
  "id": 4
}
Types
Podium
Fields
Field Name	Description
heats - [Heat]!	
name - String!	
Example
{
  "heats": [Heat],
  "name": "abc123"
}
Types
PointAllocation
Fields
Field Name	Description
id - ID!	
name - String!	
Example
{"id": 4, "name": "xyz789"}
Types
PointsPerPlaceResult
Fields
Field Name	Description
competitor - Competitor!	
place - Int!	
placeCounts - [Int]!	
total - Float!	
Example
{
  "competitor": Competitor,
  "place": 987,
  "placeCounts": [123],
  "total": 123.45
}
Types
PreviewDraw
Fields
Field Name	Description
rounds - [PreviewRound!]!	
Example
{"rounds": [PreviewRound]}
Types
PreviewHeat
Fields
Field Name	Description
numberOfCompetitors - Int!	
position - Int!	
Example
{"numberOfCompetitors": 123, "position": 987}
Types
PreviewRound
Fields
Field Name	Description
heats - [PreviewHeat!]!	
name - String!	
roundPosition - Int!	
Example
{
  "heats": [PreviewHeat],
  "name": "abc123",
  "roundPosition": 987
}
Types
PricingData
Fields
Field Name	Description
addOnBaselinePrices - [AddOnBaselinePrice!]!	
country - String	
creditBaselinePrices - [CreditBaselinePrice!]!	
currency - String!	
marketFactors - [MarketFactor!]!	
region - String!	
sizeFactors - [SizeFactor!]!	
volumeDiscounts - [Float!]!	
Example
{
  "addOnBaselinePrices": [AddOnBaselinePrice],
  "country": "abc123",
  "creditBaselinePrices": [CreditBaselinePrice],
  "currency": "abc123",
  "marketFactors": [MarketFactor],
  "region": "abc123",
  "sizeFactors": [SizeFactor],
  "volumeDiscounts": [987.65]
}
Types
Property
Fields
Field Name	Description
config - PropertyConfig	
disabled - Boolean	
docusealTemplateId - ID	
docusealTemplateSlug - String	
label - String!	
level - PropertyLevelEnum!	
organisationId - ID	
required - Boolean	
sportType - String	
type - PropertyTypeEnum!	
uuid - ID!	
value - String	
Example
{
  "config": PropertyConfig,
  "disabled": false,
  "docusealTemplateId": 4,
  "docusealTemplateSlug": "xyz789",
  "label": "xyz789",
  "level": "user",
  "organisationId": 4,
  "required": false,
  "sportType": "xyz789",
  "type": "text",
  "uuid": 4,
  "value": "xyz789"
}
Types
PropertyConfig
Fields
Field Name	Description
description - String	
docusealTemplateId - ID	
docusealTemplateSlug - String	
options - [String!]	
requireIf - RequireIf	
restricted - Boolean	
validation - Validation	
Example
{
  "description": "abc123",
  "docusealTemplateId": 4,
  "docusealTemplateSlug": "xyz789",
  "options": ["xyz789"],
  "requireIf": RequireIf,
  "restricted": false,
  "validation": Validation
}
Types
PropertyConfigInput
Description
Arguments for creating or updating configuration for an organisation custom property

Fields
Input Field	Description
options - [String!]	
docusealTemplateId - ID	
docusealTemplateSlug - String	
Example
{
  "options": ["abc123"],
  "docusealTemplateId": "4",
  "docusealTemplateSlug": "xyz789"
}
Types
PropertyInput
Description
Arguments for creating or updating an organisation custom property

Fields
Input Field	Description
uuid - ID	
label - String!	
type - PropertyTypeEnum!	
level - PropertyLevelEnum!	
required - Boolean	
options - [String!]	
deleted - Boolean	
config - PropertyConfigInput	
Example
{
  "uuid": "4",
  "label": "abc123",
  "type": "text",
  "level": "user",
  "required": true,
  "options": ["abc123"],
  "deleted": false,
  "config": PropertyConfigInput
}
Types
PropertyLevelEnum
Values
Enum Value	Description
user

athlete

registration

event_division

Example
"user"
Types
PropertyTypeEnum
Values
Enum Value	Description
text

select

checkbox

date

signature

Example
"text"
Types
PurchasedOptions
Fields
Field Name	Description
athletes - [RegisteringAthlete!]!	
Example
{"athletes": [RegisteringAthlete]}
Types
RankingFilters
Fields
Field Name	Description
property - RankingPropertyFilter	
Example
{"property": RankingPropertyFilter}
Types
RankingOptions
Fields
Field Name	Description
countingResultsOverrides - Boolean	
cutLines - [CutLine!]	
eligibleResults - JSON	
filters - RankingFilters	
Example
{
  "countingResultsOverrides": false,
  "cutLines": [CutLine],
  "eligibleResults": {},
  "filters": RankingFilters
}
Types
RankingPropertyFilter
Fields
Field Name	Description
label - String!	
value - String	
Example
{
  "label": "abc123",
  "value": "abc123"
}
Types
RankingRuleOverride
Fields
Field Name	Description
athlete - Athlete	
division - Division	
id - ID!	
override - Int	
rule - String!	
series - Series!	
Example
{
  "athlete": Athlete,
  "division": Division,
  "id": 4,
  "override": 123,
  "rule": "abc123",
  "series": Series
}
Types
RankingRuleOverrideInput
Description
arguments for creating a ranking rule override.

Fields
Input Field	Description
id - ID	
athleteId - ID	
seriesId - ID	
divisionId - ID!	
rule - String	
override - Int!	
Example
{
  "id": 4,
  "athleteId": 4,
  "seriesId": 4,
  "divisionId": 4,
  "rule": "xyz789",
  "override": 123
}
Types
Record
Types
Union Types
Team

Example
Team
Types
RecordInput
Description
Arguments for defining a record in a permission

Fields
Input Field	Description
recordType - String!	
recordId - ID!	
Example
{"recordType": "abc123", "recordId": 4}
Types
Refund
Fields
Field Name	Description
amount - Int!	
id - ID!	
status - String!	
Example
{"amount": 123, "id": 4, "status": "abc123"}
Types
RefundPaymentInput
Description
Autogenerated input type of RefundPayment

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
amount - Int!	
Example
{
  "clientMutationId": "xyz789",
  "id": "4",
  "amount": 123
}
Types
RefundPaymentPayload
Description
Autogenerated return type of RefundPayment.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
errors - String	
payment - Payment!	
Example
{
  "clientMutationId": "xyz789",
  "errors": "abc123",
  "payment": Payment
}
Types
Region
Fields
Field Name	Description
currency - String!	
name - String!	
Example
{
  "currency": "abc123",
  "name": "xyz789"
}
Types
RegisteringAthlete
Fields
Field Name	Description
extras - [Extras!]	
name - String!	
registrationsAttributes - [RegistrationsAttribute!]	
Example
{
  "extras": [Extras],
  "name": "xyz789",
  "registrationsAttributes": [RegistrationsAttribute]
}
Types
RegistrationOptions
Fields
Field Name	Description
captureProperties - [Property!]	
divisionLimit - Int	
divisions - [RegistrationOptionsDivisions!]	
notes - String	
teamRequired - Boolean	
termsAndConditionsLink - String	
termsOwner - String	
waitlisted - Boolean	
Example
{
  "captureProperties": [Property],
  "divisionLimit": 987,
  "divisions": [RegistrationOptionsDivisions],
  "notes": "abc123",
  "teamRequired": false,
  "termsAndConditionsLink": "xyz789",
  "termsOwner": "abc123",
  "waitlisted": true
}
Types
RegistrationOptionsDivisions
Fields
Field Name	Description
id - ID	
maxAge - Int	
maxBy - ISO8601Date	
minAge - Int	
minBy - ISO8601Date	
Example
{
  "id": 4,
  "maxAge": 123,
  "maxBy": ISO8601Date,
  "minAge": 987,
  "minBy": ISO8601Date
}
Types
RegistrationsAttribute
Fields
Field Name	Description
id - Int	
optionId - Int!	
Example
{"id": 123, "optionId": 123}
Types
RemoveAthleteFromHeatInput
Description
Autogenerated input type of RemoveAthleteFromHeat

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heatId - ID!	
athleteId - ID!	
Example
{
  "clientMutationId": "abc123",
  "heatId": 4,
  "athleteId": "4"
}
Types
RemoveAthleteFromHeatPayload
Description
Autogenerated return type of RemoveAthleteFromHeat.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heat - Heat!	
Example
{
  "clientMutationId": "abc123",
  "heat": Heat
}
Types
RemovePermissionFromRecordInput
Description
Autogenerated input type of RemovePermissionFromRecord

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
permissionId - ID!	
Example
{
  "clientMutationId": "xyz789",
  "permissionId": "4"
}
Types
RemovePermissionFromRecordPayload
Description
Autogenerated return type of RemovePermissionFromRecord.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
team - Team!	
Example
{
  "clientMutationId": "xyz789",
  "team": Team
}
Types
RemovePriorityInput
Description
Autogenerated input type of RemovePriority

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
competitorId - ID!	
Example
{
  "clientMutationId": "abc123",
  "competitorId": 4
}
Types
RemovePriorityPayload
Description
Autogenerated return type of RemovePriority.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heat - Heat!	
Example
{
  "clientMutationId": "xyz789",
  "heat": Heat
}
Types
RemoveUserFromOrganisationInput
Description
Autogenerated input type of RemoveUserFromOrganisation

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
organisationId - ID!	
Example
{
  "clientMutationId": "abc123",
  "id": 4,
  "organisationId": "4"
}
Types
RemoveUserFromOrganisationPayload
Description
Autogenerated return type of RemoveUserFromOrganisation.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
user - User!	
Example
{
  "clientMutationId": "abc123",
  "user": User
}
Types
RequireIf
Fields
Field Name	Description
conditions - [RequireIfCondition!]!	
operator - RequireIfOperator	
Example
{"conditions": [RequireIfCondition], "operator": "and"}
Types
RequireIfComparator
Values
Enum Value	Description
greater

less

equal

notequal

Example
"greater"
Types
RequireIfCondition
Fields
Field Name	Description
comparator - RequireIfComparator!	
property - String!	
value - String!	
Example
{
  "comparator": "greater",
  "property": "xyz789",
  "value": "xyz789"
}
Types
RequireIfOperator
Values
Enum Value	Description
and

or

Example
"and"
Types
ResetUserPasswordInput
Description
Autogenerated input type of ResetUserPassword

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
password - String!	
confirmPassword - String!	
Example
{
  "clientMutationId": "xyz789",
  "id": "4",
  "password": "abc123",
  "confirmPassword": "abc123"
}
Types
ResetUserPasswordPayload
Description
Autogenerated return type of ResetUserPassword.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
user - User!	
Example
{
  "clientMutationId": "xyz789",
  "user": User
}
Types
Restriction
Fields
Field Name	Description
type - String!	
value - StringOrInteger!	
Example
{
  "type": "abc123",
  "value": StringOrInteger
}
Types
Result
Fields
Field Name	Description
athlete - Athlete!	
dropped - Boolean	
eventDivision - EventDivision!	
id - ID!	
place - Int	
points - Int!	
Example
{
  "athlete": Athlete,
  "dropped": true,
  "eventDivision": EventDivision,
  "id": "4",
  "place": 987,
  "points": 123
}
Types
RollingMembership
Fields
Field Name	Description
currency - String	
defaultDivisionPrice - Int	
divisions - [PaymentOptionsDivisions!]	
extraDivisionPrice - Int	
extras - [PaymentExtra!]	
familyTotal - JSON	
length - Int!	
unit - String!	
Example
{
  "currency": "abc123",
  "defaultDivisionPrice": 123,
  "divisions": [PaymentOptionsDivisions],
  "extraDivisionPrice": 123,
  "extras": [PaymentExtra],
  "familyTotal": {},
  "length": 987,
  "unit": "abc123"
}
Types
SaveEventDivisionAsTemplateInput
Description
Autogenerated input type of SaveEventDivisionAsTemplate

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
name - String!	
eventDivisionId - ID!	
organisationId - ID!	
Example
{
  "clientMutationId": "abc123",
  "name": "abc123",
  "eventDivisionId": "4",
  "organisationId": 4
}
Types
SaveEventDivisionAsTemplatePayload
Description
Autogenerated return type of SaveEventDivisionAsTemplate.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivision - EventDivision	
Example
{
  "clientMutationId": "xyz789",
  "eventDivision": EventDivision
}
Types
Schedule
Fields
Field Name	Description
breaks - [Break!]	
heatsIntervalSeconds - Int!	
podiums - [Podium!]	
Example
{
  "breaks": [Break],
  "heatsIntervalSeconds": 987,
  "podiums": [Podium]
}
Types
SeededRound
Fields
Field Name	Description
round - Int!	
seeds - Int	
Example
{"round": 987, "seeds": 987}
Types
SendEventEmailInput
Description
Autogenerated input type of SendEventEmail

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventId - ID!	
subject - String!	
message - String!	
Example
{
  "clientMutationId": "abc123",
  "eventId": 4,
  "subject": "xyz789",
  "message": "abc123"
}
Types
SendEventEmailPayload
Description
Autogenerated return type of SendEventEmail.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
event - Event!	
Example
{
  "clientMutationId": "abc123",
  "event": Event
}
Types
Series
Fields
Field Name	Description
allDivisions - [Division!]!	Deprecated in favor of fetching rankingsDivision directly, this causes lots of db queries and lookups
athleteRankingResults - AthleteRankingResult	
Arguments
divisionId - ID!
athleteId - ID!
filter - String
availableRankingFilters - [String!]	
Arguments
divisionId - ID!
captureFields - [Property!]!	
childSeries - [Series!]!	
divisions - [Division!]!	Deprecated in favor of fetching specific membershipDivisions or rankingsDivision
events - [Event!]	
exclusive - Boolean!	
id - ID!	
membershipDivisions - [Division!]!	
name - String!	
options - Options	
organisation - Organisation!	
organisationId - ID!	
paginatedMemberships - Memberships	
Arguments
search - String
page - Int!
perPage - Int!
parentSeries - Series	
pointAllocationId - ID	
rankingOptions - RankingOptions	
rankings - [SeriesRank!]	
Arguments
divisionId - ID!
filter - String
rankingsDisplayProperty - JSON	
rankingsDivisions - [Division!]!	
registrationOptions - RegistrationOptions	
results - [Result!]	Deprecated in favor of athleteRankingResults which contains more information
Arguments
divisionId - ID!
athleteId - ID!
filter - String
resultsToCount - JSON	
signOnStatus - SignOnStatus!	
Example
{
  "allDivisions": [Division],
  "athleteRankingResults": AthleteRankingResult,
  "availableRankingFilters": ["abc123"],
  "captureFields": [Property],
  "childSeries": [Series],
  "divisions": [Division],
  "events": [Event],
  "exclusive": false,
  "id": 4,
  "membershipDivisions": [Division],
  "name": "xyz789",
  "options": Options,
  "organisation": Organisation,
  "organisationId": 4,
  "paginatedMemberships": Memberships,
  "parentSeries": Series,
  "pointAllocationId": 4,
  "rankingOptions": RankingOptions,
  "rankings": [SeriesRank],
  "rankingsDisplayProperty": {},
  "rankingsDivisions": [Division],
  "registrationOptions": RegistrationOptions,
  "results": [Result],
  "resultsToCount": {},
  "signOnStatus": "closed"
}
Types
SeriesRank
Fields
Field Name	Description
athlete - Athlete!	
displayProperty - String	
place - Int!	
points - Int!	
results - [Result!]!	
Example
{
  "athlete": Athlete,
  "displayProperty": "xyz789",
  "place": 987,
  "points": 987,
  "results": [Result]
}
Types
SignOnStatus
Values
Enum Value	Description
closed

open

draft

Example
"closed"
Types
SizeFactor
Fields
Field Name	Description
factor - Float!	
size - String!	
Example
{"factor": 987.65, "size": "abc123"}
Types
SportType
Values
Enum Value	Description
surf

skate

snow

sls

wake

skim

bodyboard

bmx

scooter

other

paddle

freeride

windsurf

fmb

Example
"surf"
Types
String
Description
Represents textual data as UTF-8 character sequences. This type is most often used by GraphQL to represent free-form human-readable text.

Example
"xyz789"
Types
StringOrInteger
Description
An integer or a string

Example
StringOrInteger
Types
StripeAccountDetails
Fields
Field Name	Description
chargesEnabled - Boolean!	
type - String	
Example
{"chargesEnabled": false, "type": "abc123"}
Types
Team
Fields
Field Name	Description
id - ID!	
name - String!	
permissions - [Permission!]!	
Example
{
  "id": 4,
  "name": "xyz789",
  "permissions": [Permission]
}
Types
TeamConfig
Fields
Field Name	Description
appraisalLevel - String	
athletesPerTeam - Int	
Example
{
  "appraisalLevel": "xyz789",
  "athletesPerTeam": 987
}
Types
TeamConfigInput
Description
Arguments for updating team config

Fields
Input Field	Description
athletesPerTeam - Int	
Example
{"athletesPerTeam": 987}
Types
TeamMember
Fields
Field Name	Description
athlete - Athlete!	
id - ID!	
order - Int!	
teamRoleId - ID	
teamRoleName - String	
Example
{
  "athlete": Athlete,
  "id": "4",
  "order": 987,
  "teamRoleId": 4,
  "teamRoleName": "abc123"
}
Types
TeamMemberInput
Description
Arguments for adding a team member, creating the athlete when necessary

Fields
Input Field	Description
id - ID	
order - Int	
athleteId - ID	
athlete - AthleteInput	
teamRoleId - ID	
teamRoleName - String	
_destroy - Boolean	
Example
{
  "id": 4,
  "order": 123,
  "athleteId": 4,
  "athlete": AthleteInput,
  "teamRoleId": "4",
  "teamRoleName": "xyz789",
  "_destroy": true
}
Types
TeamRole
Fields
Field Name	Description
id - ID!	
name - String!	
Example
{"id": 4, "name": "abc123"}
Types
Template
Fields
Field Name	Description
id - ID!	
name - String!	
organisationId - ID	
sportType - String	
teamRoles - [TeamRole!]	
Example
{
  "id": 4,
  "name": "xyz789",
  "organisationId": "4",
  "sportType": "abc123",
  "teamRoles": [TeamRole]
}
Types
UpdateAthleteInput
Description
Autogenerated input type of UpdateAthlete

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
id - ID!	
athlete - AthleteInput!	
Example
{
  "clientMutationId": "abc123",
  "id": "4",
  "athlete": AthleteInput
}
Types
UpdateAthletePayload
Description
Autogenerated return type of UpdateAthlete.

Fields
Field Name	Description
athlete - Athlete!	
clientMutationId - String	A unique identifier for the client performing the mutation.
Example
{
  "athlete": Athlete,
  "clientMutationId": "xyz789"
}
Types
UpdateContestInput
Description
Autogenerated input type of UpdateContest

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
contest - ContestInput!	
Example
{
  "clientMutationId": "xyz789",
  "contest": ContestInput
}
Types
UpdateContestPayload
Description
Autogenerated return type of UpdateContest.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
contest - Contest!	
eventDivision - EventDivision!	
Example
{
  "clientMutationId": "abc123",
  "contest": Contest,
  "eventDivision": EventDivision
}
Types
UpdateEventConfigInput
Description
Autogenerated input type of UpdateEventConfig

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventId - ID!	
config - EventConfigInput!	
Example
{
  "clientMutationId": "abc123",
  "eventId": 4,
  "config": EventConfigInput
}
Types
UpdateEventConfigPayload
Description
Autogenerated return type of UpdateEventConfig.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
event - Event!	
Example
{
  "clientMutationId": "abc123",
  "event": Event
}
Types
UpdateEventDivisionInput
Description
Autogenerated input type of UpdateEventDivision

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivisionId - ID!	
formatDefinition - FormatDefinitionInput	
entryLimit - EntryLimitInput	
Example
{
  "clientMutationId": "xyz789",
  "eventDivisionId": 4,
  "formatDefinition": FormatDefinitionInput,
  "entryLimit": EntryLimitInput
}
Types
UpdateEventDivisionPayload
Description
Autogenerated return type of UpdateEventDivision.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivision - EventDivision!	
Example
{
  "clientMutationId": "xyz789",
  "eventDivision": EventDivision
}
Types
UpdateMembershipInput
Description
Autogenerated input type of UpdateMembership

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
membership - MembershipUpdateInput!	
Example
{
  "clientMutationId": "abc123",
  "membership": MembershipUpdateInput
}
Types
UpdateMembershipPayload
Description
Autogenerated return type of UpdateMembership.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
membership - Membership	
Example
{
  "clientMutationId": "xyz789",
  "membership": Membership
}
Types
UpdateOrganisationInput
Description
Autogenerated input type of UpdateOrganisation

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
organisation - EditOrganisationInput!	
Example
{
  "clientMutationId": "abc123",
  "organisation": EditOrganisationInput
}
Types
UpdateOrganisationPayload
Description
Autogenerated return type of UpdateOrganisation.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
organisation - Organisation!	
Example
{
  "clientMutationId": "xyz789",
  "organisation": Organisation
}
Types
UpdateRankingRuleOverrideInput
Description
Autogenerated input type of UpdateRankingRuleOverride

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
rankingRuleOverride - RankingRuleOverrideInput!	
Example
{
  "clientMutationId": "abc123",
  "rankingRuleOverride": RankingRuleOverrideInput
}
Types
UpdateRankingRuleOverridePayload
Description
Autogenerated return type of UpdateRankingRuleOverride.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
rankingRuleOverride - RankingRuleOverride!	
Example
{
  "clientMutationId": "xyz789",
  "rankingRuleOverride": RankingRuleOverride
}
Types
UpdateRoundInput
Description
Autogenerated input type of UpdateRound

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
eventDivisionId - ID!	
roundPosition - Int!	
roundName - String!	
heatDurationMinutes - Int	
Example
{
  "clientMutationId": "abc123",
  "eventDivisionId": "4",
  "roundPosition": 987,
  "roundName": "xyz789",
  "heatDurationMinutes": 987
}
Types
UpdateRoundPayload
Description
Autogenerated return type of UpdateRound.

Fields
Field Name	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
heats - [Heat!]!	
Example
{
  "clientMutationId": "xyz789",
  "heats": [Heat]
}
Types
UpdateTeamMembersInput
Description
Autogenerated input type of UpdateTeamMembers

Fields
Input Field	Description
clientMutationId - String	A unique identifier for the client performing the mutation.
entryId - ID!	
teamMembers - [TeamMemberInput!]!	
Example
{
  "clientMutationId": "abc123",
  "entryId": 4,
  "teamMembers": [TeamMemberInput]
}
Types
UpdateTeamMembersPayload
Description
Autogenerated return type of UpdateTeamMembers.

Fields
Field Name	Description
athleteHeats - [Competitor!]!	
clientMutationId - String	A unique identifier for the client performing the mutation.
entry - Entry!	
Example
{
  "athleteHeats": [Competitor],
  "clientMutationId": "abc123",
  "entry": Entry
}
Types
User
Fields
Field Name	Description
athletes - [Athlete!]!	
competitors - [Competitor!]!	
Arguments
eventId - ID
eventDivisionId - ID
athleteId - ID
email - String!	
entries - [Entry!]!	
Arguments
eventId - ID
eventDivisionId - ID
athleteId - ID
eventAthletes - [Athlete!]!	
Arguments
eventId - ID!
eventEmails - [Email!]	
id - ID!	
image - String	
name - String	
pendingPayments - [Payment!]!	
phone - String	
properties - JSON	
role - String!	
unfinishedEvents - [Event!]!	
Example
{
  "athletes": [Athlete],
  "competitors": [Competitor],
  "email": "xyz789",
  "entries": [Entry],
  "eventAthletes": [Athlete],
  "eventEmails": [Email],
  "id": "4",
  "image": "xyz789",
  "name": "xyz789",
  "pendingPayments": [Payment],
  "phone": "abc123",
  "properties": {},
  "role": "xyz789",
  "unfinishedEvents": [Event]
}
Types
UserInput
Description
Arguments for creating an user

Fields
Input Field	Description
name - String!	
email - String!	
phone - String	
Example
{
  "name": "abc123",
  "email": "xyz789",
  "phone": "abc123"
}
Types
UserRole
Values
Enum Value	Description
director

judge

Example
"director"
Types
Validation
Fields
Field Name	Description
idName - String	
parameters - [Parameter!]	
params - [String!]	
url - String	
Example
{
  "idName": "xyz789",
  "parameters": [Parameter],
  "params": ["xyz789"],
  "url": "xyz789"
}
Documentation by Anvil SpectaQL