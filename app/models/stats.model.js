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
  this.id = manifest.id;
  this.UserEmail = stats.UserEmail;
  this.PreferenceType = stats.PreferenceType;
  this.PreferenceName = stats.PreferenceName;
  this.Data = stats.Data;

  this.ID = stats.ID;

 
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


Stats.getManifests = (id, startDate, endDate, res) => {

  console.log('startDate',startDate)
  console.log('endDate',endDate)
  console.log('id',id)

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_manifestQuery.py', startDate, endDate, id]);

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
  let query = "SELECT ID, PreferenceData FROM UserPreferences "
  
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


Stats.updateUserPreference = (UserEmail, PreferenceName, PreferenceType, ID, Data, result) => {
  
  let query = "UPDATE  UserPreferences Set UserEmail='${UserEmail}', PreferenceType='${PreferenceType}', PreferenceName='${PreferenceName}', PreferenceData='${Data}' "
      query+= "WHERE ID = '${ID}'"

  // console.log('sql',query);
  // console.log('UserEmail ',UserEmail)
  // console.log('PreferenceName ',PreferenceName)
  // console.log('PreferenceType ',PreferenceType)
  // console.log('Data ',Data)


  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    if (res.affectedRows == 0) {
      // not found Tutorial with the id
      result({ kind: "not_found" }, null);
      return;
    }

    console.log("updated user preference : ", { ID: ID, PreferenceName: PreferenceName });
    result(null, { ID: ID, PreferenceName: PreferenceName });
  });
};


Stats.createUserPreference = (UserEmail, PreferenceType, PreferenceName, Data, result) => {
  let query = `INSERT INTO UserPreferences (UserEmail, PreferenceType, PreferenceName, PreferenceData) VALUES ('${UserEmail}', '${PreferenceType}','${PreferenceName}','${Data}') `
  
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



Stats.getFlightsDashboard = (p1, p2, res) => {

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_skedflexDashboard.py', p1, p2]);

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


Stats.getAircraftStatus = (p1, res) => {

  const { spawn } = require('child_process');
  const cmd = spawn('python3', ['python/do_skedflexAcftStatus.py', p1]);

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
