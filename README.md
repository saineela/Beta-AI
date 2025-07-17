
*ONLY WORKS ON FIRST RELEASE OF PYTHON 3.9*

# Beta-AI

**An All-in-One AI Productivity Suite**

Beta-AI is a versatile artificial intelligence application designed to enhance productivity and creativity. It leverages advanced AI models to provide users with a wide array of functionalities, including:

- **Universal App Launcher**: Open any application by name.
- **Dynamic Web Search**: Access websites based on keywords or names.
- **Document & Presentation Generation**: Automatically create and save documents and presentations.
- **Image Generation**: Generate images based on conversational prompts.
- **Real-Time Knowledge Access**: Retrieve the latest information using integrated search capabilities.
- **Video Playback**: Play videos from platforms like YouTube and all the way till Linkedin anything on the internet is searchable and playable, just by Asking in Natural Language.

## Features

- **Universal App Launcher**: Launch any installed application by simply stating its name.
- **Dynamic Web Search**: Search for and open websites based on specific keywords or names.
- **Document & Presentation Generation**: Automatically generate documents and presentations tailored to your needs and save them directly to your desktop.
- **Image Generation**: Create images from textual descriptions to enhance your projects.
- **Real-Time Knowledge Access**: Utilize integrated search capabilities to access the latest information from the web.
- **Video Playback**: Play videos from platforms like YouTube and LinkedIn by providing relevant keywords or video titles.

## Installation

To set up Beta-AI on your local machine, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/saineela/Beta-AI.git
   cd Beta-AI


2. **Set Up Environment Variables**:

   Fill the details in the `.env` file in the root directory and add the following variables:

   ```env
   CohereAPIKey=your_cohere_api_key
   GroqAPIKey=your_groq_api_key
   HuggingFaceAPIKey=your_huggingface_api_key
   ```

   Replace `your_cohere_api_key`, `your_groq_api_key`, and `your_huggingface_api_key` with your actual API keys.

   **How to Obtain API Keys**:

   * **Cohere**: Sign in to your Cohere account, navigate to the API Keys section, and click "Create an API Key" to generate a new key.
   * **Groq**: Visit the Groq Cloud Console, sign in or create an account, go to the Developers section, and click "Create API Key" to generate a new key.
   * **Hugging Face**: Log in to your Hugging Face account, go to your profile settings, and under the "Access Tokens" section, click "Generate New API Key" to create a new key.

3. **Install Dependencies**:

   ```bash
   pip install -r ./requirements.txt
   ```

4. **Run the Application**:

   ```bash
   python Main.py
   ```

   The application will start, and you can access it through your preferred interface.

## Usage

Upon running the application, you can interact with Beta-AI through its user interface. Input your commands or prompts, and Beta-AI will process them using its integrated AI models and provide the desired outputs.

## Contributing

We welcome contributions to Beta-AI! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

Please ensure that your contributions align with the project's goals and adhere to the coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* **Cohere**: For providing advanced language models.
* **Groq**: For offering high-performance AI processing capabilities.
* **Hugging Face**: For hosting a wide range of machine learning models.
