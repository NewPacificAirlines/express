const sql = require("./db.js");

// constructor

const { spawn } = require("child_process");
const { end } = require("./db.js");


const Stats = function(stats){
  this.startDate = stats.startDate;
  this.endDate = stats.endDate;
  this.flightnum = stats.flightnum;
  this.p1 = stats.startDate;
  this.p2 = stats.endDate;
  this.p3 = stats.flightnum;
  this.p4 = stats.tails;
  this.Manifestid = manifest.id;


  this.UserEmail = stats.UserEmail;
  this.PreferenceType = stats.PreferenceType;
  this.PreferenceName = stats.PreferenceName;
  this.PreferenceID = stats.PreferenceID;
  this.Data = stats.Data;
  this.FilterData = stats.FilterData;
  this.origin = stats.origin;
  this.dest = stats.dest;


  this.StatsId = stats.ID;

 
}



// const pythonParams = function(params){
//   this.paramOne = params.startDate;
//   this.paramTwo = params.endDate
// }


Stats.getFlights = (p1, p2, p3, p4, res) => {

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_skedflexQuery.py', p1, p2, p3, p4]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });
};


Stats.getManifests = (Manifestid, startDate, endDate, res) => {

  console.log('startDate',startDate)
  console.log('endDate',endDate)
  console.log('Manifestid',Manifestid)

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_manifestQuery.py', startDate, endDate, Manifestid]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });


};


Stats.getAircraft = (active, result) => {
  let query = "SELECT aircraft, short, type FROM Aircraft"
  // console.log('sql',query);
  
  if (active !== undefined ) {
    query += ` WHERE active = '${active}'`;
  }

  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    // console.log("aircraft: ", res);
    result(null, res);
  });
};


Stats.getAllUserPreferences = (UserEmail, PreferenceType, result) => {
  let query = "SELECT PreferenceName FROM UserPreferences "
  
  query += ` WHERE UserEmail = '${UserEmail}' AND PreferenceType = '${PreferenceType}'`;
  // console.log('sql',query);


  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    result(null, res);
  });
};


Stats.getUserPreferenceByName = (UserEmail, PreferenceName, PreferenceType, result) => {
  let query = "SELECT ID, PreferenceData, FilterData FROM UserPreferences "
  
  query += ` WHERE UserEmail = '${UserEmail}' AND PreferenceName = '${PreferenceName}' AND PreferenceType = '${PreferenceType}'`;
  // console.log('sql',query);


  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    result(null, res);
  });
};


Stats.updateUserPreference = (PreferenceID,Data, FilterData, result) => {
  
  let query = "UPDATE  UserPreferences SET FilterData='"+FilterData+"', PreferenceData='"+Data+"'"
      query+= " WHERE ID = '"+PreferenceID+"'"

  // console.log('sql',query);

  // console.log('PreferenceID ',PreferenceID)
  // console.log('Data ',Data)
  // console.log('FilterData ',FilterData) 

  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    if (res.affectedRows == 0) {
      // not found Tutorial with the id
      console.log("error: ", err);
      result({ kind: "not_found" }, null);
      return;
    }

    // result(null, { ID: ID, PreferenceName: PreferenceName });
    result(null, res);
  });
};


Stats.createUserPreference = (UserEmail, PreferenceType, PreferenceName, Data, FilterData, result) => {
  let query = `INSERT INTO UserPreferences (UserEmail, PreferenceType, PreferenceName, PreferenceData, FilterData) VALUES ('${UserEmail}', '${PreferenceType}','${PreferenceName}','${Data}','${FilterData}') `
  
  // console.log('sql',query);
  

  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    result(null, res);
  });
};


Stats.deleteUserPreference = (ID, result) => {
  sql.query("DELETE FROM UserPreferences WHERE id = ?", ID, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    if (res.affectedRows == 0) {
      // not found UserPreference with the id
      result({ kind: "not_found" }, null);
      return;
    }

    console.log("deleted user preference with id: ", ID);
    result(null, res);
  });
};



Stats.getFlightsDashboard = (p1, p2, p3, res) => {

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_skedflexDashboard.py', p1, p2, p3]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });
};


Stats.getCargoDashboard = (p1, p2, res) => {

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_cargoQuery.py', p1, p2]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });
};


Stats.getAircraftStatus = (p1,p2, res) => {

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_skedflexAcftStatus.py', p1, p2]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });
};


Stats.getCargoData = (startDate,endDate,origin,dest, res) => {

  console.log('getCargoData startDate ',startDate)
  console.log('getCargoData endDate ',endDate)

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_cargoDataQuery.py', startDate, endDate, origin, dest]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });
};


Stats.getCargoDetailData = (DetailID, res) => {

   // console.log('getOtherCharges DetailID ',DetailID)


  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_cargoDetailQuery.py', DetailID]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });
};


Stats.getWhizTicketData = (DetailID, res) => {

  console.log('getWhizTicketData startDate ',startDate)
  console.log('getWhizTicketData endDate ',endDate)

  
 const { spawn } = require('child_process');
 const cmd = spawn('python3', ['python/do_cargoWhizQuery.py', startDate, endDate]);

 let bufferArray= []

 // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
 
 cmd.stdout.on('data', (data) => {
   // console.log(`stdout: ${data}`);
   bufferArray.push(data)
 });
 
 cmd.stderr.on('data', (data) => {
   console.error(`stderr: ${data}`);
 });
 
 cmd.on('close', (code) => {
   console.log(`child process exited with code ${code}`);
   let dataBuffer =  Buffer.concat(bufferArray);
   // console.log(dataBuffer.toString());
   res(null, dataBuffer);
 });
};


Stats.getOtherCharges = (DetailID, res) => {

  // console.log('getOtherCharges DetailID ',DetailID)

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_getOtherCharges.py', DetailID]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });
};


Stats.getAirports = (active, result) => {
  let query = "SELECT DOT, Name FROM Airports "
  // console.log('sql',query);
  
  if (active !== undefined ) {
    query += ` WHERE Active = '${active}'`;
  }

  query += ` ORDER BY DOT`;

  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    // console.log("airports: ", res);
    result(null, res);
  });
};


Stats.getTimezones = (result) => {
  let query = "SELECT * FROM Timezones ORDER BY timezone DESC;"
  // console.log('sql',query);
  
  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    // console.log("timezones: ", res);
    result(null, res);
  });
};

Stats.getPrinters = (location, result) => {
  
  let query = "SELECT name, ip_address, location, type, description, port FROM Printers "

  console.log('location',location)
  
  if (location !== undefined ) {
    query += ` WHERE location = '${location}'`;
  }

  query += ` ORDER BY name`;

  console.log('sql',query);

  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    console.log("Printers: ", res);
    result(null, res);
  });
};


Stats.printBagTag = (printer,legs,company,tagNumber,recordLoc,flightDate,lastName,firstName,fullDest,fullState,flight1,dest1,flight2,dest2,dest2Dep,flight3,dest3,dest3Dep,flight4,dest4,dest4Dep,selectee,returnData,rush,res) => {
    
  // console.log('Printer IP',printer)
 

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/create_BTPFile.py',printer,legs,company,tagNumber,recordLoc,flightDate,lastName,firstName,fullDest,fullState,flight1,dest1,flight2,dest2,dest2Dep,flight3,dest3,dest3Dep,flight4,dest4,dest4Dep,selectee,returnData,rush]);

  let bufferArray= []

  // cmd.stdout.setEncoding('utf8'); sets encdoing defualt encoding is buffer
  
  cmd.stdout.on('data', (data) => {
    // console.log(`stdout: ${data}`);
    bufferArray.push(data)
  });
  
  cmd.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  cmd.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });
};

module.exports = Stats;
