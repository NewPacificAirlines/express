module.exports = app => {

  
  const stats = require("../controllers/stats.controller.js");


  var router = require("express").Router();

  // Retrieve all Stats with condition
  router.get("/aircraft", stats.getAircraft);


  // Get post to run python script
  router.get("/python", stats.getFlights);


  // Get post to get manifest detail
  router.get("/manifest", stats.getManifests);

  //Post post to create new user preference

  router.post("/userpreference", stats.CreateUserPreference);

  //Get post to get user preferences by user and type

  router.get("/alluserpreference", stats.FindAllUserPreference);

  //Get post to get user preferences by user type and preferencename

  router.get("/userpreference", stats.FindUserPreference);

  //Post post to update user preference or create new one is none exists.

  router.post("/updateuserpreference", stats.UpdateUserPreference);

 //Post post to create user preference or create new one is none exists.

  router.post("/createuserpreference", stats.CreateUserPreference);

//Post post to delete user preference or create new one is none exists.

  router.post("/deleteuserpreference", stats.DeleteUserPreference);

//Get to retrieve skedflex data for Dashboard

 // Get post to run python script
 router.get("/dashboard_getFlightDataNew", stats.getFlightsDashboard);

// Get post to run python script
router.get("/dashboard_getCargoDataNew", stats.getCargoDashboard);

// Get post to run python script
router.get("/getCargoData", stats.getCargoData);

// Get post to run python script
router.get("/getCargoDetailData", stats.getCargoDetailData);

// Get post to run python script
router.get("/getOtherCharges", stats.getOtherCharges);


// Get post to run python script
router.get("/getAirports", stats.getAirports);


// Get post to run python script
router.get("/dashboard_getAircraftStatus", stats.getAircraftStatus);

  app.use('/api/', router);
};
