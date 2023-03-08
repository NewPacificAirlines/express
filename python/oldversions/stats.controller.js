
const Stats = require("../models/stats.model.js");

// const Formpost = require("../models/stats.model.js");

const date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();
let currentDate = `${year}-${month}-${day}`;



// Handle calls to python script

exports.runPython = (req, res) => {

  console.log('req.query',req.query)

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
  

    Stats.runPython(startDate, endDate, flightNum, tails, (err, data) => {
      if (err)
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving stats."
        });
      else res.send(data);
    });
  else
    res.status(500).send('Error Missing Security Key!')

};


// Retrieve all active Aircraft records from the database 
exports.getAircraft = (req, res) => {
  const active = req.query.active;
  const ravnKey = '08a853e59b398fc84577489bcd03fb53e5db892c'

  const key = req.query.key;

  console.log('req.query',req.query)

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


// // Create and Save a Form Post
// exports.formPost = (req, res) => {
//   // Validate request
//   if (!req.body) {
//     res.status(400).send({
//       message: "Content can not be empty!"
//     });
//   }
//   console.log('request: ',req.body);

//   // Create a Save Post Object

 
//   const formPost = new Formpost({
//     name: req.body.name,
//     emailOffers: req.body.emailOffers || false,
//     interfaceStyle: req.body.interfaceStyle,
//     subscriptionType: req.body.subscriptionType,
//     notes: req.body.notes,
//     toggle: req.body.toggle,
//     startDate: req.body.startDate,
//     endDate: req.body.endDate

//   });
 

//   console.log('formPost:', formPost)
  
//   // Save Form Post in the database
//   Stats.create(formPost, (err, data) => {
//     if (err)
//       res.status(500).send({
//         message:
//           err.message || "Some error occurred while creating the Form Post."
//       });
//     else res.send(data);
//     // else res.status(400).send({
//     //   message: "Some bad data from client!"
//     // });


//   });
// };


// // Create and Save a new Tutorial
// exports.create = (req, res) => {
//   // Validate request
//   if (!req.body) {
//     res.status(400).send({
//       message: "Content can not be empty!"
//     });
//   }

//   // Create a Tutorial
//   const tutorial = new Tutorial({
//     title: req.body.title,
//     description: req.body.description,
//     published: req.body.published || false,
//     date: req.body.date || currentDate
//   });
  
//   // Save Tutorial in the database
//   Tutorial.create(tutorial, (err, data) => {
//     if (err)
//       res.status(500).send({
//         message:
//           err.message || "Some error occurred while creating the Tutorial."
//       });
//     else res.send(data);
//   });
// };

// // Retrieve all Tutorials from the database (with condition).
// exports.findCondition = (req, res) => {
//   const title = req.query.title;
//   const date = req.query.date;

//   Tutorial.getAll(title, date, (err, data) => {
//     if (err)
//       res.status(500).send({
//         message:
//           err.message || "Some error occurred while retrieving tutorials."
//       });
//     else res.send(data);
//   });
// };




// // Find a single Tutorial by Id
// exports.findOne = (req, res) => {
//   Tutorial.findById(req.params.id, (err, data) => {
//     if (err) {
//       if (err.kind === "not_found") {
//         res.status(404).send({
//           message: `Not found Tutorial with id ${req.params.id}.`
//         });
//       } else {
//         res.status(500).send({
//           message: "Error retrieving Tutorial with id " + req.params.id
//         });
//       }
//     } else res.send(data);
//   });
// };




// // find all published Tutorials
// exports.findAllPublished = (req, res) => {
//   Tutorial.getAllPublished((err, data) => {
//     if (err)
//       res.status(500).send({
//         message:
//           err.message || "Some error occurred while retrieving tutorials."
//       });
//     else res.send(data);
//   });
// };

// // Update a Tutorial identified by the id in the request
// exports.update = (req, res) => {
//   // Validate Request
//   if (!req.body) {
//     res.status(400).send({
//       message: "Content can not be empty!"
//     });
//   }

//   console.log(req.body);

//   Tutorial.updateById(
//     req.params.id,
//     new Tutorial(req.body),
//     (err, data) => {
//       if (err) {
//         if (err.kind === "not_found") {
//           res.status(404).send({
//             message: `Not found Tutorial with id ${req.params.id}.`
//           });
//         } else {
//           res.status(500).send({
//             message: "Error updating Tutorial with id " + req.params.id
//           });
//         }
//       } else res.send(data);
//     }
//   );
// };

// // Delete a Tutorial with the specified id in the request
// exports.delete = (req, res) => {
//   Tutorial.remove(req.params.id, (err, data) => {
//     if (err) {
//       if (err.kind === "not_found") {
//         res.status(404).send({
//           message: `Not found Tutorial with id ${req.params.id}.`
//         });
//       } else {
//         res.status(500).send({
//           message: "Could not delete Tutorial with id " + req.params.id
//         });
//       }
//     } else res.send({ message: `Tutorial was deleted successfully!` });
//   });
// };

// // Delete all Tutorials from the database.
// exports.deleteAll = (req, res) => {
//   Tutorial.removeAll((err, data) => {
//     if (err)
//       res.status(500).send({
//         message:
//           err.message || "Some error occurred while removing all tutorials."
//       });
//     else res.send({ message: `All Tutorials were deleted successfully!` });
//   });
// };
