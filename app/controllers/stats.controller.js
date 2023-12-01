
const { end } = require("../models/db.js");
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
  const FilterData = req.query.FilterData;

  const Data = req.query.Data;


  // console.log('CreateUserPreference req.query',req.query)


  if (key == ravnKey)

  Stats.createUserPreference(UserEmail,PreferenceType,PreferenceName,Data,FilterData, (err, data) => {
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
  const PreferenceID = req.query.ID;
  const Data = req.query.Data;
  const FilterData = req.query.FilterData;

  console.log('PreferenceID ',PreferenceID)


  if (key == ravnKey)

  Stats.updateUserPreference(PreferenceID,Data,FilterData, (err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while updating preference."
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

  startDate = '2020-11-01';
  const todayDate = new Date();
  let day = todayDate.getDate();
  let month = todayDate.getMonth() + 1;
  let year = todayDate.getFullYear();
  let endDate = `${year}-${month}-${day}`;

  if ( req.query.startDate != null)
    startDate = req.query.startDate

  if ( req.query.endDate != null)  
    endDate = req.query.endDate

  if (req.query.utc != null)
    utc = req.query.utc
  else
    utc = 'no'  


  // console.log('startDate ',startDate)
  // console.log('endDate ',endDate)


  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  
  
  if (key == ravnKey)
  

    Stats.getFlightsDashboard(startDate, endDate, utc, (err, data) => {
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


exports.getCargoDashboard = (req, res) => {

  console.log('getStats.req.query',req.query)

  startDate = '2020-11-01';
  const todayDate = new Date();
  let day = todayDate.getDate();
  let month = todayDate.getMonth() + 1;
  let year = todayDate.getFullYear();
  let endDate = `${year}-${month}-${day}`;

  if ( req.query.startDate != null)
    startDate = req.query.startDate

  if ( req.query.endDate != null)  
    endDate = req.query.endDate


  // console.log('startDate ',startDate)
  // console.log('endDate ',endDate)

  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  
  
  if (key == ravnKey)
  

    Stats.getCargoDashboard(startDate, endDate, (err, data) => {
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


exports.getAircraftStatus = (req, res) => {

  console.log('getStats.req.query',req.query)

 
  const today = new Date()
  

  let day = today.getDate();
  let month = String(today.getMonth() + 1).padStart(2,"0");
  let year = today.getFullYear();
  let defaultStart = `${year}-${month}-${day}`;

  if ( req.query.startDate != null)
    startDate = req.query.startDate
  else;
    startDate = defaultStart

  const tomorrow = new Date(today)
  tomorrow.setDate(tomorrow.getDate() + 1)
  day = tomorrow.getDate();
  month = String(tomorrow.getMonth() + 1).padStart(2,"0");
  year = tomorrow.getFullYear();
  let defaultEnd = `${year}-${month}-${day}`;

  if ( req.query.endDate != null)
    endDate = req.query.startDate
  else;
    endDate = defaultEnd


  console.log('startDate ',startDate)
  console.log('endDate ',endDate)

  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  
  
  if (key == ravnKey)
  

    Stats.getAircraftStatus(startDate, endDate, (err, data) => {
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

exports.getCargoData = (req, res) => {

  console.log('getCargoData.req.query',req.query)

  const startDate = req.query.startdate;
  const endDate = req.query.enddate;
  const origin = req.query.origin;
  const dest = req.query.dest;

  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  
  // console.log('controller key ',ravnKey)
  // console.log('controller startDate ',startDate)
  // console.log('controller endDate ',endDate)
  
  if (key == ravnKey)
  

    Stats.getCargoData(startDate, endDate, origin, dest, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving cargo."
        });
      else res.send(data)
      // console.log(data)
      
    });
  else
    res.status(500).send('Error Missing Security Key!')

};


exports.getCargoDetailData = (req, res) => {

  console.log('getCargoDetailData.req.query',req.query)

  const DetailID = req.query.ID;


  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  

  // console.log('controller startDate ',startDate)
  // console.log('controller endDate ',endDate)
  
  if (key == ravnKey)
  

    Stats.getCargoDetailData(DetailID, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving cargo detail."
        });
      else res.send(data)
      // console.log(data)
      
    });
  else
    res.status(500).send('Error Missing Security Key!')

};

exports.getWhizTicketData = (req, res) => {

  console.log('getWhizTicketData.req.query',req.query)

  const startDate = req.query.startdate;
  const endDate = req.query.enddate;


  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  

  console.log('controller DetailID ',DetailID)
  
  if (key == ravnKey)
  

    Stats.getWhizTicketData(startDate, endDate, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving whiz detail."
        });
      else res.send(data)
      // console.log(data)
      
    });
  else
    res.status(500).send('Error Missing Security Key!')

};


exports.getOtherCharges = (req, res) => {

  console.log('getOtherCharges.req.query',req.query)

  const DetailID = req.query.ID;


  const key = req.query.key;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c';
  const message = 'Error';
  

  // console.log('controller startDate ',startDate)
  // console.log('controller endDate ',endDate)
  
  if (key == ravnKey)
  

    Stats.getOtherCharges(DetailID, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving other charges detail."
        });
      else res.send(data)
      // console.log(data)
      
    });
  else
    res.status(500).send('Error Missing Security Key!')

};


// Retrieve all active Aiports records from the database 
exports.getAirports = (req, res) => {
  const active = req.query.active;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'

  const key = req.query.key;

  // console.log('getAirports.req.query',req.query)

  if (key == ravnKey)

  Stats.getAirports(active, (err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving airports."
      });
    else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 
};


// Retrieve all Timezone records from the database 
exports.getTimezones = (req, res) => {

  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'

  const key = req.query.key;

  console.log('getTimezones.req.query',req.query)

  if (key == ravnKey)

  Stats.getTimezones((err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving timezones."
      });
    else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 
};


// Retrieve all printers from database by location
exports.getPrinters = (req, res) => {

  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'
  const location = req.query.location;


  const key = req.query.key;

  console.log('getPrinters.req.query',req.query)

  if (key == ravnKey)

  Stats.getPrinters(location, (err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving printers."
      });
    else res.send(data);
  });

  else
    res.status(500).send({
      message:
        err.message || "No security key!"
    }); 
};

// Print BagTag
exports.printBagTag = (req, res) => {
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'

  const key = req.query.key;
  
  const printer = req.query.printer;
  
  const legs = req.query.legs;

  const company = req.query.company
  const tagNumber = req.query.tagNumber;
  const tagNumberLong = req.query.tagNumberLong

  const recordLoc = req.query.recordLoc;
  const flightDate = req.query.flightDate;

  const lastName = req.query.lastName;
  const firstName = req.query.firstName;
  const fullDest = req.query.fullDest;
  const fullState = req.query.fullState;


  const flight1 = req.query.flight1;
  const dest1 = req.query.dest1;
  
  const flight2 = req.query.flight2;
  const dest2 = req.query.dest2;
  const dest2Dep = req.query.dest2Dep;

  const flight3 = req.query.flight3;
  const dest3 = req.query.dest3;
  const dest3Dep = req.query.dest3Dep;

  const flight4 = req.query.flight4;
  const dest4 = req.query.dest4;
  const dest4Dep = req.query.dest4Dep;

  const returnData = req.query.returnData;

  const selectee = req.query.selectee;
  const rush  = req.query.rush;


  // console.log('printBagTag req.query',req.query)


  if (key == ravnKey){

    valid = false

    switch(Number(legs)){

      case 1:

        if (company !== '' && tagNumber !== '' && recordLoc !== '' && flightDate !== '' && lastName !== '' && firstName !== '' && fullDest !== '' && fullState !== '' && flight1 !== '' && dest1 !== '')
          valid = true
        
      case 2:
        if (company !== '' && tagNumber !== '' && recordLoc !== '' && flightDate !== '' && lastName !== '' && firstName !== '' && fullDest !== '' && fullState !== '' && flight1 !== '' && dest1 !== '' && flight2 !== '' && dest2 !== '' && dest2Dep !== '')
          valid = true
      
      case 3: 
        if (company !== '' && tagNumber !== '' && recordLoc !== '' && flightDate !== '' && lastName !== '' && firstName !== '' && fullDest !== '' && fullState !== '' && flight1 !== '' && dest1 !== '' && flight2 !== '' && dest2 !== '' && dest2Dep !== '' && flight3 !== '' && dest3 !== '' && dest3Dep !== '')
        valid = true

      case 4: 
        if (company !== '' && tagNumber !== '' && recordLoc !== '' && flightDate !== '' && lastName !== '' && firstName !== '' && fullDest !== '' && fullState !== '' && flight1 !== '' && dest1 !== '' && flight2 !== '' && dest2 !== '' && dest2Dep !== '' && flight3 !== '' && dest3 !== '' && dest3Dep !== '' && flight4 !== '' && dest4 !== '' && dest4Dep !== '')
        valid = true
    };
    
    if(valid == true){

      Stats.printBagTag(printer,legs,company,tagNumber,recordLoc,flightDate,lastName,firstName,fullDest,fullState,flight1,dest1,flight2,dest2,dest2Dep,flight3,dest3,dest3Dep,flight4,dest4,dest4Dep,selectee,returnData,rush, (err, data) => {
        if (err)
          res.status(500).send({
            message:
              err.message || "Some error occurred while creating print job."
          });
        else res.send(data);
      });

    } else {

      res.status(500).send('Error Missing Required Parameters!');

    }  

  } else {
  
    res.status(500).send('Error Missing Security Key!');

  }
};
