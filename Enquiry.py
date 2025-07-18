<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AXE Health Enquiry</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet" />
  <style>
    :root {
      --axe-blue: #003f7f;
      --axe-light: #f5f9ff;
      --axe-accent: #0073e6;
    }
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      font-family: 'Inter', sans-serif;
      background-color: var(--axe-light);
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    .form-card {
      background: white;
      padding: 40px;
      border-radius: 10px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 600px;
    }
    .form-card h1 {
      color: var(--axe-blue);
      margin-bottom: 10px;
    }
    .form-card p {
      color: #555;
      margin-bottom: 30px;
    }
    label {
      font-weight: 600;
      margin-top: 20px;
      display: block;
    }
    input, select, textarea {
      width: 100%;
      padding: 12px;
      margin-top: 8px;
      border: 1px solid #ccc;
      border-radius: 6px;
      font-size: 14px;
    }
    button {
      background: var(--axe-accent);
      color: white;
      border: none;
      padding: 14px;
      font-weight: bold;
      margin-top: 30px;
      width: 100%;
      font-size: 16px;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.3s ease;
    }
    button:hover {
      background: #005bb5;
    }
    .logo {
      display: block;
      margin: 0 auto 30px;
      max-height: 60px;
    }
  </style>
</head>
<body>
  <div class="form-card">
    <img src="logo.png" alt="AXE Health Logo" class="logo">
    <h1>Enquire with AXE Health</h1>
    <p>We’ll direct your message to the most relevant team.</p>
    <form action="thank-you.html" method="GET" onsubmit="return handleSubmit(event)">
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

      <label for="name">Name</label>
      <input type="text" id="name" name="name" required />

      <label for="email">Email</label>
      <input type="email" id="email" name="email" required />

      <label for="message">Message</label>
      <textarea id="message" name="message" rows="5" required></textarea>

      <button type="submit">Send Enquiry</button>
    </form>
  </div>

  <script>
    const brandToEmail = {
      farmaforce: "farmaforce@yourdomain.com",
      pharmaprograms: "pharmaprograms@yourdomain.com",
      precisionhealth: "precision@yourdomain.com",
      wellness: "wellness@yourdomain.com",
      sinapse: "sinapse@yourdomain.com",
      praxhub: "praxhub@yourdomain.com"
    };

    function handleSubmit(e) {
      e.preventDefault();
      const form = e.target;
      const brand = form.brand.value;
      const mailto = `mailto:${brandToEmail[brand]}?subject=AXE%20Health%20Enquiry&body=Name:%20${encodeURIComponent(form.name.value)}%0AEmail:%20${encodeURIComponent(form.email.value)}%0AMessage:%20${encodeURIComponent(form.message.value)}`;
      window.location.href = mailto;
      setTimeout(() => {
        window.location.href = form.action;
      }, 500);
      return false;
    }
  </script>
</body>
</html>
