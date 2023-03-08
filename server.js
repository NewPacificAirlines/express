const express = require("express");
// const bodyParser = require("body-parser"); /* deprecated */
const cors = require("cors");

const app = express();

const bodyParser = require("body-parser");
const {spawn} = require("child_process");
const fs = require("fs");
const https = require('https');
const http = require('http');

const options = {
  key: fs.readFileSync("app/config/star_ravnalaska_net.key"),
  cert: fs.readFileSync("app/config/star_ravnalaska_net.crt"),
};

// var corsOptions = {
//   // origin: "http://localhost:8080",
//   origin: "http://localhost:8091",
//   origin:"http://localhost:4200"
// };

app.use(cors());

// parse requests of content-type - application/json
app.use(express.json()); /* bodyParser.json() is deprecated */

// parse requests of content-type - application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true })); /* bodyParser.urlencoded() is deprecated */

// simple route
app.get("/", (req, res) => {
  res.json({ message: "Welcome to New Stats Server." });
  // res.sendFile(`${__dirname}/public/index.html`)
});



require("./app/routes/stats.routes.js")(app);

// set port, listen for requests
// const PORT = process.env.PORT || 8090;
// app.listen(PORT, () => {
//   console.log(`Server is running on port ${PORT}.`);
// });


// app.use((req, res, next) => {
//   res.send('<h1>HTTPS is working!</h1>');
// });

const secureport = 8443;

https.createServer(options, app).listen(secureport, () => {
  console.log('Server listening on port ' + secureport);
});

const port = 8077;

http.createServer(options, app).listen(port, () => {
  console.log('Server listening on port ' + port);
});