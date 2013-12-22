### The Bugle Index

This is a project to provide [The Bugle Podcast](http://thebuglepodcast.com/) with an index to the subjects and terms contained within its episodes. The index includes both real people and topics such as elections, the Pope and Silvio Berlusconi as well as things that [Andy Zaltzman](http://www.andyzaltzman.co.uk/) makes up. Your contributions are welcomed.

#### Current State

Right now this is a Python app (Django) that runs on Heroku purely as an admin interface for data entry. This repository contains not only that code but also will house the guidelines for contributing to the index (which requires that you listen to a podcast episode and then add entries to the app).


#### Definitions

* Episode - one uniquely numbered Bugle podcast. We count sub-episodes or supplemental Bugles as episodes.
* Speaker - usually either Andy Zaltzman or John Oliver, but also includes occasional guests such as "The American" and the various producers.
* Segment - a portion of an episode that begins with an introduction, such as "Silvio Berlusconi does something crazy news now!" or "Feature Section". We use that phrase (minus the "news now" bit) or title for the segment. Segments are tied to episodes.
* Subject - a person or topic mentioned. Examples include "cricket", "Osama bin Laden", "Armenia", or some fictional person or institution that Andy has dreamed up. A single subject could be mentioned many times across episodes.
* Mention - the combination of a subject and a segment within an episode.

#### Contributing

If you'd like to contribute, send an email to thebugleindex@gmail.com and we'll get you signed up for an account with the admin. From there, you can pick an episode and get started. Here's how:

1. Listen to the episode. Be prepared to replay lots of it.
2. Add the episode to the admin.
3. Each time you come to a new segment of the episode, create a new Segment record and, if necessary, a new Subject and/or Speaker.
4. Create a new Mention for each Subject discussed in a Segment. Some Segments may have multiple subjects; create a new Mention for each.

Finally, while this is an index, there are some oddities about it. First, there will be nonsensical entities reflected in it. Second, you'll need to use your judgment about certain matters. For example, should Andy's pun runs be a Subject, a Segment, or should there be a flag on a Segment record that indicates a pun run happened in it? Please use the [Issues](https://github.com/dwillis/thebugleindex/issues) to raise and discuss such questions. Common sense and consensus should prevail.

#### Questions

* Who are you?

  I'm Derek Willis, @derekwillis.

* Why are you doing this?

  Because I'm a fan.

Others? Tweet at us at @thebugleindex or send an email to thebugleindex@gmail.com.
