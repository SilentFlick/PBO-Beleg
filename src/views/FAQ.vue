<template>
  <div class="container-fluid">
    <h1>FAQ</h1>

    <div class="accordion w-50 mx-auto" id="accordionPanelsStayOpenExample">
      <div class="accordion-item">
        <h2 class="accordion-header" id="panelsStayOpen-headingOne">
          <button
            class="accordion-button"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#panelsStayOpen-collapseOne"
            aria-expanded="true"
            aria-controls="panelsStayOpen-collapseOne"
          >
            What is HTW Shit Talks?
          </button>
        </h2>
        <div
          id="panelsStayOpen-collapseOne"
          class="accordion-collapse collapse show"
          aria-labelledby="panelsStayOpen-headingOne"
        >
          <div class="accordion-body">
            <strong>HTW Shit Talks </strong> is a platform for students at HTW
            Dresden to share their experiences and opinions about the
            university. The purpose of the website is to help professors and
            lecturers improve the learning experience at the university, as well
            as provide a way for students to communicate with professors and
            lecturers. The platform is anonymous for students and is free to
            use.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#panelsStayOpen-collapseTwo"
            aria-expanded="false"
            aria-controls="panelsStayOpen-collapseTwo"
          >
            How to use it?
          </button>
        </h2>
        <div
          id="panelsStayOpen-collapseTwo"
          class="accordion-collapse collapse"
          aria-labelledby="panelsStayOpen-headingTwo"
        >
          <div class="accordion-body">
            To use <strong>HTW Shit Talks</strong> , students can log in with
            their HTW account to access full features. These features include
            the ability to write posts, like and comment on other posts, and
            search for posts by title and content. <br />

            Please note that login is only used to authenticate real people and
            that data will not be shared with third parties or stored in the
            database. Only professors and lecturers' names will be displayed on
            posts, while other posts and comments will display fake names.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="panelsStayOpen-headingThree">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#panelsStayOpen-collapseThree"
            aria-expanded="false"
            aria-controls="panelsStayOpen-collapseThree"
          >
            If I have problem, who can I contact?
          </button>
        </h2>
        <div
          id="panelsStayOpen-collapseThree"
          class="accordion-collapse collapse"
          aria-labelledby="panelsStayOpen-headingThree"
        >
          <div class="accordion-body">
            If you have any problems or want to contribute to the development of
            HTW Shit Talks, you can contact us at
            <a href="abc@xyz.com" class="text-decoration-none">abc@xyz.com</a>
            or visit our
            <a
              href="https://github.com/SilentFlick/PBO-Beleg"
              class="text-decoration-none"
              >Github repository</a
            >
            to create an issue or make a pull request.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
