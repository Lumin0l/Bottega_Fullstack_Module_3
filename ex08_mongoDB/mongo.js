/* We use these kind of editors to use mongo because it's kind of hard to write in the mongo process, learned it the hard way */

/* This is how we create userst in mongoDB */
db.createUser({
  user: 'jon',
  pwd: 'password',
  customData: { startDate: new Date() },
  roles: [
    { role: 'clusterAdmin', db: 'admin' },
    { role: 'readAnyDatabase', db: 'admin' },
    'readWrite'
  ]
})

/* To visualize the users we use: db.getUsers() and to delete a user db.dropUser('name_of_user') */

/* To create a collection we use: db.createCollection('name_of_collection') and to see it: show collections */

/* Inserting a document into mongodb database */
db.books.insert({			// First database object and then the name of the collection
	"name": "OOP Programming",
	"PublishingDate": new Date(),
	"authors": [
		{"name": "John Snow"},
		{"name": "NEd Stark" },
		]
	})

/* How to insert many documents in one go */
db.books.insertMany([
	{
		"name": "Ruby Intro",
		"publishedDate": new Date(),
		"authors: [
			{"name": "Avdi Grimm" }
			]
	},
	{
                "name": "Ruby Intro",
                "publishedDate": new Date(),
                "authors: [
                        {"name": "Avdi Grimm" }
                        ]
        },
	{
                "name": "Ruby Intro",
                "publishedDate": new Date(),
                "authors: [
                        {"name": "Avdi Grimm" }
                        ]
        },
	{
                "name": "C Intro",
                "publishedDate": new Date(),
                "authors: [
                        {"name": "Peter Grimm" }
                        ]
        },
	{
                "name": "Python Intro",
                "publishedDate": new Date(),
                "authors: [
                        {"name": "John Grimm" }
                        ]
        }

])






