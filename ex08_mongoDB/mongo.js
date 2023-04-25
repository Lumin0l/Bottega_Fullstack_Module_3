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

/* To visualize the users we use: db.getUsers() and to delete a user db.dropUser('name_of_user')
