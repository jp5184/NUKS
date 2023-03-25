<template>
  <div>
    <h1>RESTAURANT RATINGS</h1>
    <div>
      <h2>Add a new restaurant:</h2>
      <label for="newRestaurantName">Name: </label>
      <input type="text" id="newRestaurantName" v-model="newRestaurantName">
      <button @click="addRestaurant">Add</button>
    </div>
    <div>
      <h2>Add a rating:</h2>
      <label for="restaurantDropdown">Restaurant: </label>
      <select id="restaurantDropdown" v-model="selectedRestaurantId">
        <option disabled value="">Please select a restaurant</option>
        <option v-for="item in items" :value="item.id" :key="item.id">{{ item.restaurant_name }}</option>
      </select>
      <br>
      <label for="newRating">Rating: </label>
      <input type="number" id="newRating" min="1" max="5" v-model="newRating">
      <button @click="addRating">Add</button>
    </div>
    <h2>Restaurants:</h2>
    <ul>
      <li v-for="item in mergedItems" :key="item.id">
        {{ item.restaurant_name }}: {{ item.rating ? item.rating.toFixed(1) : 'No ratings yet' }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      ratings: [],
      newRestaurantName: '',
      newRestaurantAddress: '',
      newRatingRestaurantId: '',
      newRating: ''
    }
  },
  computed: {
    mergedItems() {
      // Merge the items and ratings arrays based on restaurant ID
      return this.items.map(item => {
        const filteredRatings = this.ratings.filter(rating => rating.restaurant_id === item.id);
        const averageRating = filteredRatings.reduce((acc, curr) => acc + curr.rating, 0) / filteredRatings.length;
        return {
          ...item,
          rating: filteredRatings.length > 0 ? parseFloat(averageRating.toFixed(1)) : ''
        };
      });
    }
  },
  methods: {
    addRestaurant() {
      const url = 'http://212.101.137.114:8000/addRestaurant';
      const data = {
        restaurant_name: this.newRestaurantName,
        address: this.newRestaurantAddress
      };
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(data => {
          this.items.push(data);
          this.newRestaurantName = '';
          this.newRestaurantAddress = '';
          this.refreshData();
        })
        .catch(error => {
          console.error('Error adding new restaurant:', error);
        });
    },
    addRating() {
      const url = 'http://212.101.137.114:8000/addRestaurantRating';
      const data = {
        restaurant_id: this.selectedRestaurantId,
        rating: parseInt(this.newRating)
      };
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(data => {
          this.ratings.push(data);
          this.selectedRestaurantId = '';
          this.newRating = '';
          this.refreshData();
        })
        .catch(error => {
          console.error('Error adding new rating:', error);
        });
    },
    refreshData() {
      const restaurantNameListUrl = 'http://212.101.137.114:8000/getRestaurantNameList';
      const restaurantRatingsUrl = 'http://212.101.137.114:8000/getRestaurantRatingList';

      // Fetch data from both APIs simultaneously using Promise.all()
      Promise.all([
        fetch(restaurantNameListUrl).then(response => response.json()),
        fetch(restaurantRatingsUrl).then(response => response.json())
      ]).then(data => {
        this.items = data[0];
        this.ratings = data[1];
      });
    }
  },
  mounted() {
    this.refreshData();
  }
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  margin-left: 5%;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
