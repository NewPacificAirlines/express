module.exports = app => {

  
  const stats = require("../controllers/stats.controller.js");


  var router = require("express").Router();

  //Get to get Aircraft
  router.get("/aircraft", stats.getAircraft);

  //Get to get Flights
  router.get("/python", stats.getFlights);

  // Get to get manifest detail
  router.get("/manifest", stats.getManifests);

  //Post to create new user preference
  router.post("/userpreference", stats.CreateUserPreference);

  //Get to get user preferences by user and type
  router.get("/alluserpreference", stats.FindAllUserPreference);

  //Get to get user preferences by user type and preferencename
  router.get("/userpreference", stats.FindUserPreference);

  //Post to update user preference or create new one is none exists.
  router.post("/updateuserpreference", stats.UpdateUserPreference);

  //Post to create user preference.
  router.post("/createuserpreference", stats.CreateUserPreference);

  //Post to delete user preference.
  router.post("/deleteuserpreference", stats.DeleteUserPreference);

  //Get to retrieve skedflex data for Dashboard
  router.get("/dashboard_getFlightDataNew", stats.getFlightsDashboard);

  // Get to get Cargo Data for Dashboard
  router.get("/dashboard_getCargoDataNew", stats.getCargoDashboard);

  // Get to get Cargo Data for Cargo App
  router.get("/getCargoData", stats.getCargoData);

  // Get to get Cargo Detail for a specific record
  router.get("/getCargoDetailData", stats.getCargoDetailData);

  // Get to Other Charges for a specific record
  router.get("/getOtherCharges", stats.getOtherCharges);

  // Get to get list of Airports
  router.get("/getAirports", stats.getAirports);

  // Get to get list of Timezones
  router.get("/getTimezones", stats.getTimezones);

  // Get to get Aircraft Status
  router.get("/dashboard_getAircraftStatus", stats.getAircraftStatus);

  // Get to get list of Printers by Location
  router.get("/getPrinters", stats.getPrinters);

  // Send BagTag Print Job
  router.post("/printBagTag", stats.printBagTag);


app.use('/api/', router);
};
