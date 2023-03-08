const sql = require("./db.js");

// constructor

const { spawn } = require("child_process");


const Stats = function(stats){
  this.startDate = stats.startDate;
  this.endDate = stats.endDate;
  this.flightnum = stats.flightnum;
  this.p1 = stats.startDate;
  this.p2 = stats.endDate
  this.p3 = stats.flightnum
  this.p4 = stats.tails

 
}



// const pythonParams = function(params){
//   this.paramOne = params.startDate;
//   this.paramTwo = params.endDate
// }


Stats.runPython = (p1, p2, p3, p4, res) => {

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




Stats.getAircraft = (active, result) => {
  let query = "SELECT aircraft, short, type FROM Aircraft"
  console.log('sql',query);
  
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


module.exports = Stats;
// module.exports = Formpost;