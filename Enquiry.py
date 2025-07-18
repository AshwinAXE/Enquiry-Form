<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AXE Health Enquiry</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --axe-blue: #003f7f;
      --axe-accent: #0073e6;
      --axe-bg: #f5f9ff;
    }
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      padding: 0;
      font-family: 'Inter', sans-serif;
      background: var(--axe-bg);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .form-container {
      background: #fff;
      padding: 40px;
      border-radius: 10px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
      max-width: 600px;
      width: 100%;
    }
    .form-container h1 {
      margin-top: 0;
      color: var(--axe-blue);
      font-size: 24px;
    }
    .form-container p {
      color: #555;
      margin-bottom: 30px;
    }
    label {
      font-weight: 600;
      display: block;
      margin: 20px 0 8px;
    }
    input, select, textarea {
      width: 100%;
      padding: 12px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 6px;
    }
    button {
      width: 100%;
      padding: 14px;
      margin-top: 30px;
      font-size: 16px;
      background: var(--axe-accent);
      color: #fff;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.3s ease;
    }
    button:hover {
      background: #005bb5;
    }
    .logo {
      max-height: 60px;
      margin-bottom: 20px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <img src="logo.png" alt="AXE Health Logo" class="logo">
    <h1>Enquire with AXE Health</h1>
    <p>Please select the brand you wish to contact. We'll route your message accordingly.</p>
    <form id="enquiryForm">
      <label for="brand">Brand</label>
      <select id="brand" name="brand" required>
        <option value="">-- Select a brand --</option>
        <option value="farmaforce">Farmaforce</option>
        <option value="pharmaprograms">PharmaPrograms</option>
        <option value="precisionhealth">Precision Health</option>
        <option value="wellness">Wellness</option>
        <option value="sinapse">Sinapse Health</option>
        <option value="praxhub">Praxhub</option>
      </select>

      <label for="name">Your Name</label>
      <input type="text" id="name" name="name" required>

      <label for="email">Your Email</label>
      <input type="email" id="email" name="email" required>

      <label for="message">Your Message</label>
      <textarea id="message" name="message" rows="5" required></textarea>

      <button type="submit">Send Enquiry</button>
    </form>
  </div>

  <script>
    const brandEmails = {
      farmaforce: "farmaforce@yourdomain.com",
      pharmaprograms: "pharmaprograms@yourdomain.com",
      precisionhealth: "precision@yourdomain.com",
      wellness: "wellness@yourdomain.com",
      sinapse: "sinapse@yourdomain.com",
      praxhub: "praxhub@yourdomain.com"
    };

    document.getElementById('enquiryForm').addEventListener('submit', function(e) {
      e.preventDefault();

      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const message = document.getElementById('message').value;
      const brand = document.getElementById('brand').value;
      const recipient = brandEmails[brand];

      if (!recipient) {
        alert("Please select a brand.");
        return;
      }

      const mailto = `mailto:${recipient}?subject=AXE Health Enquiry&body=Name: ${encodeURIComponent(name)}%0AEmail: ${encodeURIComponent(email)}%0AMessage: ${encodeURIComponent(message)}`;
      window.location.href = mailto;

      setTimeout(() => {
        window.location.href = "thank-you.html";
      }, 300);
    });
  </script>
</body>
</html>
