<template>
  <div class="container-fluid">
    <h1>Create a Post</h1>

    <body>
      <div>
        <!-- Faculty selection -->
        <select v-model="faculty" id="faculty">
          <option v-for="option in faculty_options" v-bind:value="option.id">
            {{ option.text }}
          </option>
        </select>

        <!-- Major selection -->
        <select id="vehicle-models" v-model="major">
          <option v-for="option in major_options[faculty]" :value="option.id" :key="option.id">
            {{ option.text }}
          </option>
        </select>
      </div>

      <hr>

      <div>
        <!-- Module selection -->
        <select v-model="modul" id="module">
          <option v-for="option in module_options[major]" v-bind:value="option.id">
            {{ option.text }}
          </option>

        </select>  
        <br>
        <!-- Professor selection -->
        <v-text-field id="professor" v-model="professor">
          <option v-for="option in professor_options[modul]" :value="option.id" :key="option.id">
            {{ option.text }}
          </option>
        </v-text-field>
      </div>

      <br>
      <!-- Titel or clickbait for post -->
      <div id="titel">
        <input type="text" v-model="titelTextField" placeholder="Titel" />
      </div>

      <br>
      <!-- Study Type to choose for the Post -->
      <div id="studyType">
        <input type="radio" id="lecture" value="lecture" name="StudyType">
        <label for="lecture">
          Lecture
        </label>
        <input type="radio" id="pracExercise" value="pracExercise" name="StudyType">
        <label for="pracExercise">
          Practical exercise
        </label> <input type="radio" id="theoExercise" value="theoExercise" name="StudyType">
        <label for="theoExercise">
          Theoretical Exercise
        </label>
      </div>
    </body>
  </div>
</template>

<script>
var module_options = {
  11: [
    { text: "D611 - Design Practice 1", id: 1 },
    { text: "D612 - Design Exploration", id: 2 },
    { text: "D621 - Design Practice 2", id: 3 },
    { text: "D622 - Design Studies", id: 4 },
    { text: "D623 - Pre-Master", id: 5 },
    { text: "W098 - Existenzgründung und Designrecht für die Kreativwirtschaft ", id: 6 }
  ]
};

var professor_options = {
  1: [{ text: "Prof. Dipl.-Des. Marcus Keichel" }],
  2: [{ text: "Prof. Dipl.-Des. Sebastian Schmieg" }],
  3: [{ text: "Prof. Dipl.-Des. Diana Simon" }],
  4: [{ text: "Prof. Dr. phil. Florian Alexander Schmidt" }],
  5: [{ text: "Prof. Dipl.-Des. Marcus Keichel" }],
  6: [{ text: "Prof. Dr. iur. Thorsten Richter" }],

};

var faculty_options = [
  { text: "Informatik/Mathematik", id: 1 },
  { text: 'Maschinenbau', id: 2 },
  { text: 'Design', id: 3 },
  { text: 'Elektrotechnik', id: 4 },
  { text: 'Wirtschaftswissenschaften', id: 5 },
  { text: 'Bauingenieurwesen', id: 6 },
  { text: 'Geoinformation', id: 7 },
  { text: 'Landbau/Umwelt/Chemie', id: 8 }
];


var major_options = {
  5: [
    { text: "Betriebwirtschaft", id: 1 },
    { text: "International Business", id: 2 },
    { text: "International Managment", id: 3 },
    { text: "Management mittelständischer Unternehmen", id: 4 },
    { text: "Wirtschaftsingenieurwesen", id: 5 }
  ],

  6: [
    { text: "Bauingenieurwesen", id: 6 },
    { text: "Environmental Engineering", id: 7 },
    { text: "Infrastrukturmanagement", id: 8 },
    { text: "Nachhaltiges Ertüchtigen und Bauen im Bestand", id: 9 },
  ],

  3: [
    { text: "Produkt- und Kommunikation", id: 10 },
    { text: "Products and Interactions", id: 11 },
  ],

  4: [
    { text: "Elektrotechnik/Informationstechnik", id: 12 },
    { text: "Elektrotechnik/Kommunikationstechnik", id: 13 },
    { text: "Electrical Engineering", id: 14 },
    { text: "Elektrotechnik", id: 15 },
    { text: "Elektrotechnik/Electrical Engineering", id: 16 },
  ],

  6: [
    { text: "Geoinformatik/Management", id: 17 },
    { text: "Geomatik: Vermessung/Kartographie/Geoinformatik", id: 18 },
    { text: "Vermessungswesen", id: 19 },
  ],

  1: [
    { text: "Angewandte Informatik", id: 20 },
    { text: "Informatik", id: 21 },
    { text: "Medieninformatik", id: 22 },
    { text: "Verwaltungsinformatik", id: 23 },
    { text: "Wirtschaftsinformatik", id: 24 },
  ],

  8: [
    { text: "Agrarwirtschaft", id: 25 },
    { text: "Chemieingenieurwesen", id: 26 },
    { text: "Gartenbau", id: 27 },
    { text: "Landschaftsentwicklung", id: 28 },
    { text: "Produktionsgartenbau", id: 29 },
    { text: "Produktionsmanagement Agrarwirtschaft", id: 30 },
    { text: "Umweltmonitoring", id: 31 },
  ],

  2: [
    { text: "Allgemeiner Maschinenbau", id: 32 },
    { text: "Fahrzeugtechnik", id: 33 },
    { text: "Gebäudesystemtechnik", id: 34 },
    { text: "Produktionstechnik", id: 35 }
  ]
};



export default {

  data() {
    return {
      titelTextField: '',
      faculty: null,
      major: null,
      professor: null,
      modul: null,
      faculty_options: faculty_options,
      major_options: major_options,
      professor_options: professor_options,
      module_options: module_options
    }
  },
}
</script>