const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const  cors = require('cors')
const app = express()
const port = 3030;

app.use(cors())
app.use(require('body-parser').urlencoded({ extended: false }));

const reviews_data = JSON.parse(fs.readFileSync("reviews.json", 'utf8'));
const dealerships_data = JSON.parse(fs.readFileSync("dealerships.json", 'utf8'));

mongoose.connect("mongodb://mongo_db:27017/",{'dbName':'dealershipsDB'});


const Reviews = require('./review');

const Dealerships = require('./dealership');

try {
  Reviews.deleteMany({}).then(()=>{
    Reviews.insertMany(reviews_data['reviews']);
  });
  Dealerships.deleteMany({}).then(()=>{
    Dealerships.insertMany(dealerships_data['dealerships']);
  });
  
} catch (error) {
  res.status(500).json({ error: 'Error fetching documents' });
}


// Express route to home
app.get('/', async (req, res) => {
    res.send("Welcome to the Mongoose API")
});

// Express route to fetch all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const documents = await Reviews.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch reviews by a particular dealer
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const documents = await Reviews.find({dealership: req.params.id});
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch all dealerships
app.get('/fetchDealers', async (req, res) => {
  try {
    const documents = await Dealerships.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch Dealers by a particular state
app.get('/fetchDealers/:state', async (req, res) => {
//Write your code here
    try {
    const state = req.params.state;

    // Dealers que pertenezcan al estado recibido
    const dealers = await Dealerships.find({ state: state });

    if (dealers.length === 0) {
      return res.status(404).json({ message: `No se encontraron dealers en el estado: ${state}` });
    }

    res.json(dealers);
  } catch (error) {
    console.error("Error fetching dealers:", error);
    res.status(500).json({ message: "Error interno del servidor" });
  }
});

// Express route to fetch dealer by a particular id
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    const idAsNumber = Number(req.params.id);
    const idAsString = req.params.id;

    // el id recibido es un ObjectId válido?
    let idAsObjectId = null;
    if (mongoose.Types.ObjectId.isValid(idAsString)) {
      idAsObjectId = new mongoose.Types.ObjectId(idAsString);
    }

    console.log("ID recibido:", idAsString, 
                "| como número:", idAsNumber, 
                "| como ObjectId:", idAsObjectId);

    //filtro dinámico
    const orConditions = [
      { id: idAsString },   // id como string
      { id: idAsNumber }    // id como number
    ];

    if (idAsObjectId) {
      orConditions.push({ _id: idAsObjectId }); // _id de Mongo
    }

    // Buscar un solo dealer
    const documents = await Dealerships.findOne({ $or: orConditions });
    console.log("Resultado query:", documents);

    if (!documents) {
      return res.status(404).json({ error: `No se encontró un dealer con id: ${idAsString}` });
    }

    res.json(documents);
  } catch (error) {
    console.error("Error al obtener dealer:", error);
    res.status(500).json({ error: 'Error fetching dealer' });
  }
});

//Express route to insert review
app.post('/insert_review', express.raw({ type: '*/*' }), async (req, res) => {
  data = JSON.parse(req.body);
  const documents = await Reviews.find().sort( { id: -1 } )
  let new_id = documents[0]['id']+1

  const review = new Reviews({
		"id": new_id,
		"name": data['name'],
		"dealership": data['dealership'],
		"review": data['review'],
		"purchase": data['purchase'],
		"purchase_date": data['purchase_date'],
		"car_make": data['car_make'],
		"car_model": data['car_model'],
		"car_year": data['car_year'],
	});

  try {
    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
		console.log(error);
    res.status(500).json({ error: 'Error inserting review' });
  }
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
