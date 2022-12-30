const sql = require("./db.js");

// constructor

const { spawn } = require("child_process");


const Stats = function(stats){
  this.startDate = stats.startDate;
  this.endDate = stats.endDate;
  this.flightnum = stats.flightnum
}

Stats.getAll = (startDate, endDate, flightNum, result) => {
  let query = "SELECT * FROM SkedFlexData";

  if (flightNum !== undefined ) {
    query += ` WHERE flightnum LIKE '%${flightNum}%'`;
  }

  if ((startDate !== undefined) & (endDate !== undefined)) {
    query += ` WHERE date BETWEEN '${startDate}' AND '${endDate}'`;
  }



  sql.query(query, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    console.log("stats: ", res);
    result(null, res);
  });
};


const pythonParams = function(params){
  this.paramOne = params.startDate;
  this.paramTwo = params.endDate
}


Stats.runPython = (paramOne, paramTwo, res) => {

  const { spawn } = require('child_process');
  const cmd = spawn("python3", ["python/do_skedflexQuery.py", paramOne, paramTwo]);
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
    // console.log(`child process exited with code ${code}`);
    let dataBuffer =  Buffer.concat(bufferArray);
    // console.log(dataBuffer.toString());
    res(null, dataBuffer);
  });


};

// Tutorial.create = (newTutorial, result) => {
//   sql.query("INSERT INTO tutorials SET ?", newTutorial, (err, res) => {
//     console.log(newTutorial);
//     if (err) {
//       console.log("error: ", err);
//       result(err, null);
//       return;
//     }

//     console.log("created tutorial: ", { id: res.insertId, ...newTutorial });
//     result(null, { id: res.insertId, ...newTutorial });
//   });
// };

// Tutorial.findById = (id, result) => {
//   sql.query(`SELECT * FROM tutorials WHERE id = ${id}`, (err, res) => {
//     if (err) {
//       console.log("error: ", err);
//       result(err, null);
//       return;
//     }

//     if (res.length) {
//       console.log("found tutorial: ", res[0]);
//       result(null, res[0]);
//       return;
//     }

//     // not found Tutorial with the id
//     result({ kind: "not_found" }, null);
//   });
// };



// Tutorial.getAll = (title, date, result) => {
//   let query = "SELECT * FROM tutorials";

//   if (title !== undefined ) {
//     query += ` WHERE title LIKE '%${title}%'`;
//   }

//   if (date !== undefined) {
//     query += ` WHERE date LIKE '%${date}%'`;
//   }

//   sql.query(query, (err, res) => {
//     if (err) {
//       console.log("error: ", err);
//       result(null, err);
//       return;
//     }

//     console.log("tutorials: ", res);
//     result(null, res);
//   });
// };


// Tutorial.getDate = (date, result) => {
//   let query = "SELECT * FROM tutorials";

//   if (title) {
//     query += ` WHERE date LIKE '%${date}%'`;
//   }

//   sql.query(query, (err, res) => {
//     if (err) {
//       console.log("error: ", err);
//       result(null, err);
//       return;
//     }

//     console.log("tutorials: ", res);
//     result(null, res);
//   });
// };

// Tutorial.getAllPublished = result => {
//   sql.query("SELECT * FROM tutorials WHERE published=true", (err, res) => {
//     if (err) {
//       console.log("error: ", err);
//       result(null, err);
//       return;
//     }

//     console.log("tutorials: ", res);
//     result(null, res);
//   });
// };

// Tutorial.updateById = (id, tutorial, result) => {
//   sql.query(
//     "UPDATE tutorials SET title = ?, description = ?, published = ? WHERE id = ?",
//     [tutorial.title, tutorial.description, tutorial.published, id],
//     (err, res) => {
//       if (err) {
//         console.log("error: ", err);
//         result(null, err);
//         return;
//       }

//       if (res.affectedRows == 0) {
//         // not found Tutorial with the id
//         result({ kind: "not_found" }, null);
//         return;
//       }

//       console.log("updated tutorial: ", { id: id, ...tutorial });
//       result(null, { id: id, ...tutorial });
//     }
//   );
// };

// Tutorial.remove = (id, result) => {
//   sql.query("DELETE FROM tutorials WHERE id = ?", id, (err, res) => {
//     if (err) {
//       console.log("error: ", err);
//       result(null, err);
//       return;
//     }

//     if (res.affectedRows == 0) {
//       // not found Tutorial with the id
//       result({ kind: "not_found" }, null);
//       return;
//     }

//     console.log("deleted tutorial with id: ", id);
//     result(null, res);
//   });
// };

// Tutorial.removeAll = result => {
//   sql.query("DELETE FROM tutorials", (err, res) => {
//     if (err) {
//       console.log("error: ", err);
//       result(null, err);
//       return;
//     }

//     console.log(`deleted ${res.affectedRows} tutorials`);
//     result(null, res);
//   });
// };

// module.exports = Tutorial;


module.exports = Stats;