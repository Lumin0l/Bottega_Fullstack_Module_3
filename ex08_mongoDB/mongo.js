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

/* Find methods and SQL equivalents */

db.books.find().pretty() // This will return every book we created. With pretty it will be better formated.

// In SQL this would be "SELECT * from books"

/* Select a particular document */
db.books.find( {name: "OOP Programming"} ).pretty() // So you use the find function and you introduce the object.

// In SQL this would be "SELECT * from books WHERE name = "OOP Programming"" 


/* MongoDB projections */
db.books.find(
	{
	    name: "Confident Ruby"
	}, 
	// This thing up there will bring all atributes, but if we want extra atributes we need to specify:
	{
	    name: 1,
	    pubishedDate:1,
	} 
  ).pretty() // This way we will only get the elements we flagged with 1.
// In SQL "SELECT name, authors FROM books WHERE name = 'Confident Ruby'"

/* Query for a nested array, only requesting some elements from an object */
// Let's insert another element:
db.books.insert({
  "name": "Blink",
  "publishedDate": new Date(),
  "authors": [
    { "name": "Malcolm Gladwell" },
    { "name": "Ghost Writer" }
  ]
});

// Now let's look for it with the "find" function and the "slice" functionality we saw in python:
db.books.find(
  {
    name: "Blink"
  },
  {
    publishedDate: 1,
    name: 1,
    authors: { $slice: 1 } // This will use slice with the index 1, because in the end of the day authors in the dictionary is just an array.
  }
).pretty()

/* How to delete stuff */
// Several ways:
db.books.find({name: "OOP Programming"}) // This will delete everything.
db.books.remove({name: "OOP Programming"}, 1) // This removes a single document.


/* How to include nested divs in a find query */
db.books.find(
    {
	name: "Blink"
    },
    {
	name: 1,
	publishedDate: 1,
	"authors.name": 1
    }
).pretty() 
// This will limit the output to the key stablished with the "authors.name"



