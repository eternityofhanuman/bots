# Deploying Your React Frontend to Netlify

1. **Push your code to GitHub (or GitLab/Bitbucket).**
2. **Go to [Netlify](https://app.netlify.com/) and click "Add new site" > "Import an existing project".**
3. **Connect your repository.**
4. **Set the build command:**
   ```
   cd frontend && npm install && npm run build
   ```
5. **Set the publish directory:**
   ```
   frontend/dist
   ```
6. **(Optional) Add environment variables in Netlify dashboard if needed.**
7. **Click "Deploy site".**

Your React app will be live on a Netlify URL!

---

**Note:**
- The backend (API, bot) is not deployed on Netlify. For backend, use services like Render, Railway, Heroku, or your own server.
- For custom domains, use Netlify’s domain management after deployment.
