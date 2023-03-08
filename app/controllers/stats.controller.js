
const Stats = require("../models/stats.model.js");

// const Formpost = require("../models/stats.model.js");

const date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();
let currentDate = `${year}-${month}-${day}`;



// Handle calls to python script

exports.getFlights = (req, res) => {

  console.log('getStats.req.query',req.query)

  const startDate = req.query.startdate;
  const endDate = req.query.enddate;
  const flightNum = req.query.flightnum;
  const tails = req.query.tails;
  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  

  // console.log('flightNum',flightNum);
  // console.log('tails',tails)  

  // const tailNum = '';
  
  if (key == ravnKey)
  

    Stats.getFlights(startDate, endDate, flightNum, tails, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving stats."
        });
      else res.send(data)
      
    });
  else
    res.status(500).send('Error Missing Security Key!')

};

//Retrieve Manifests

exports.getManifests = (req, res) => {

  console.log('getManifests.req.query',req.query)

  const id = req.query.id;
  const key = req.query.key;

  const startDate = req.query.startDate;
  const endDate = req.query.endDate;

  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  

  console.log('startDate ',startDate)
  console.log('endDate ',endDate)
  console.log('id ',id)

  if (key == ravnKey)
  
    Stats.getManifests(id, startDate, endDate, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving manifest."
        });
      else {res.send(data)
      // console.log('Returned Data ',JSON.stringify(data))
      };
    });
  else
    res.status(500).send('Error Missing Security Key!')

};


// Retrieve all active Aircraft records from the database 
exports.getAircraft = (req, res) => {
  const active = req.query.active;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'

  const key = req.query.key;

  // console.log('getAircraft.req.query',req.query)

  if (key == ravnKey)

  Stats.getAircraft(active, (err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving aircraft."
      });
    else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 
};


// Create and Save a new User Preference
exports.CreateUserPreference = (req, res) => {
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'

  const key = req.query.key;
  const UserEmail = req.query.UserEmail;
  const PreferenceType = req.query.PreferenceType;
  const PreferenceName = req.query.PreferenceName;
  const Data = req.query.Data;


  // console.log('CreateUserPreference req.query',req.query)


  if (key == ravnKey)

  Stats.createUserPreference(UserEmail,PreferenceType,PreferenceName,Data, (err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving preference."
      });
    else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 
};

// Find a single User Preference by ID
exports.FindUserPreference = (req, res) => {
  
};


// Update a User Preference by the id in the request
exports.UpdateUserPreference = (req, res) => {
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'

  const key = req.query.key;
  const ID = req.query.ID;
  const UserEmail = req.query.UserEmail;
  const PreferenceType = req.query.PreferenceType;
  const PreferenceName = req.query.PreferenceName;
  const Data = req.query.Data;


  // console.log('CreateUserPreference req.query',req.query)


  if (key == ravnKey)

  Stats.updateUserPreference(UserEmail,PreferenceType,PreferenceName,ID,Data, (err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating preference."
      });
    else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 
};


// Find all User Preferences by type and user
exports.FindAllUserPreference = (req, res) => {
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'
  const key = req.query.key;
  const UserEmail = req.query.UserEmail;
  const PreferenceType = req.query.PreferenceType

  // console.log('FindAllUserPreference.req.query',req.query)

  if (key == ravnKey)

    Stats.getAllUserPreferences(UserEmail, PreferenceType, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving user preferences."
        });
      else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 

};

// Get User Preference by UserEmail PreferenceName and PreferenceType
exports.FindUserPreference = (req, res) => {
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'
  const key = req.query.key;
  const UserEmail = req.query.UserEmail;
  const PreferenceName = req.query.PreferenceName
  const PreferenceType = req.query.PreferenceType

  // console.log('FindAllUserPreference.req.query',req.query)

  if (key == ravnKey)

    Stats.getUserPreferenceByName(UserEmail, PreferenceName, PreferenceType, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving user preferences."
        });
      else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 

};

// Update or create user preference

exports.UpdateUserPreference = (req, res) => {
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'
  const key = req.query.key;
  const UserEmail = req.query.UserEmail;
  const PreferenceName = req.query.PreferenceName
  const PreferenceType = req.query.PreferenceType
  const ID = req.query.ID
  const Data = req.query.Data

  if (!req.body) {
    res.status(400).send({
      message: "Content can not be empty!"
    });
  }

  // console.log('UpdateUserPreference.req.query',req.query)
  // console.log('req.query.Body',Body)


  if (key == ravnKey)

    Stats.updateUserPreference(UserEmail, PreferenceName, PreferenceType, ID, Data, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving user preferences."
        });
      else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 

};
// Get User Preference by UserEmail PreferenceName and PreferenceType
exports.DeleteUserPreference = (req, res) => {
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'
  const key = req.query.key;
  const ID = req.query.ID

  // console.log('FindAllUserPreference.req.query',req.query)

  if (key == ravnKey)

    Stats.deleteUserPreference(ID, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while deleting user preferences."
        });
      else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 

};

// Handle calls to python script for Dashboard calls

exports.getFlightsDashboard = (req, res) => {

  console.log('getStats.req.query',req.query)

  const startDate = '2020-11-01';
  
  const todayDate = new Date();
  let day = todayDate.getDate();
  let month = todayDate.getMonth() + 1;
  let year = todayDate.getFullYear();
  let endDate = `${year}-${month}-${day}`;

  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  

  // console.log('flightNum',flightNum);
  // console.log('tails',tails)  

  // const tailNum = '';
  
  if (key == ravnKey)
  

    Stats.getFlightsDashboard(startDate, endDate, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving stats."
        });
      else res.send(data)
      
    });
  else
    res.status(500).send('Error Missing Security Key!')

};