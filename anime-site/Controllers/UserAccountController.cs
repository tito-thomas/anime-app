using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Policy;
using System.Web;
using System.Web.Mvc;
using anime_site.Models;
using System.Security.Cryptography;
using System.Web.Helpers;
using Microsoft.Ajax.Utilities;
using System.Web.Security;
using System.Collections;
using Newtonsoft.Json;
using System.Diagnostics;

namespace anime_site.Controllers
{

    public class UserAccountController : Controller
    {

        public ActionResult Register()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Register(UserDetails user)
        {
            if (ModelState.IsValid) { //model is invalid if one or more fields are blank
                using (MyDbContext db = new MyDbContext()) {
                    //If the username is taken, try again
                    if (db.userAccount.Any(i => i.username == user.username))
                    {
                        ViewBag.Warning = "This username is taken, please try again";
                        return View();
                    }
                    //Password validation
                    //still need to hash
                    else if (user.password.Length < 7)
                    { 
                      ViewBag.Warning = "Password must be at least 7 characters"; 
                      return View();
                    }
                    else if (user.ConfirmPassword == null)
                    {
                        ViewBag.Warning = "Please confirm your password";
                        return View();
                    }
                    else if (user.password != user.ConfirmPassword)
                    {
                        ViewBag.Warning = "Passwords do not match";
                        return View();
                    }
                    else
                    {

                        //Hash password
                        var password_hash = Crypto.HashPassword(user.password);
                        user.password = password_hash;
                        user.IsNew = true;
                        db.userAccount.Add(user);
                        db.SaveChanges();
                        ModelState.Clear();
                        ViewBag.SuccessMessage = user.username + " registered";
                        return RedirectToAction("Login", "UserAccount");
                    }                       
                }
            }
            else{ViewBag.Warning = "Please confirm your password";}
            
            return View();
        }

        public ActionResult Login()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Login(UserDetails user)
        {
            {
                
                if (ModelState.IsValid) //model is invalid if one or more fields are blank
                {
                    using (MyDbContext db = new MyDbContext())
                    {
                        //var current_hashed = Crypto.HashPassword(user.password);
                        //var auth = db.RegAccount.Where(i => i.username.Equals(user.username) && i.password.Equals(user.password)).FirstOrDefault();
                        var username_auth = db.userAccount.Where(i => i.username.Equals(user.username)).FirstOrDefault();
                        if (username_auth != null)
                        {
                            var pass_auth = Crypto.VerifyHashedPassword(username_auth.password, user.password);

                            if (pass_auth == true)
                            {
                                Session["username"] = user.username;
                                FormsAuthentication.SetAuthCookie(user.username, true);
                                //If the user is new, pass argument that leads to first-time questions being asked
                                if (username_auth.IsNew)
                                {
                                    //Save user details to persistent cookie
                                    UserDetailsDto fields = new UserDetailsDto
                                    {
                                        userId = username_auth.userId,
                                        username = username_auth.username,
                                        IsNew = username_auth.IsNew
                                    };
                                    string data_string = JsonConvert.SerializeObject(fields);
                                    HttpCookie usercookie = new HttpCookie("usercookie", data_string);
                                    usercookie.Expires = DateTime.Now.AddDays(1);
                                    Response.Cookies.Add(usercookie);
                             
                                    return RedirectToAction("Dashboard", "UserAccount", new {new_user = true});
                                }
                                return RedirectToAction("Dashboard", "UserAccount");
                            }
                            else
                            {
                                ViewBag.Message = "Incorrect username or password";
                                return View();
                            }
                        }
                        else
                        {
                            ViewBag.Message = "Incorrect username or password";
                            return View();
                        }
                    }
                }
                return View();
            }

        }

        public ActionResult Logout() 
        {
            FormsAuthentication.SignOut();
            Session.Clear();
            Session.Abandon();
            return RedirectToAction("Index","Home")
                
;       }

        /*public ActionResult CreateVector(FormCollection form)
        {
            var v1 = Request.Form["v1"];
            var v2 = Request.Form["v2"];
            var v3 = Request.Form["v3"];
            var v4 = Request.Form["v4"];
            var v5 = Request.Form["v5"];
            //string vector_values = v1+v2+

            return RedirectToAction("Dashboard","Home", new { new_user = false });
        }*/

        public ActionResult Dashboard(bool new_user = true)
        {
            if (new_user)
            {
                ViewBag.Welcome1 = "Hi there, welcome to the recommendation platform!";
                ViewBag.Welcome2 = "Before you get started please answer a few questions so we can learn what interests you.";
                return View();
            }
            return View();
 
        }
        [HttpPost]
        public ActionResult Dashboard(NewQuestions form)
        {
            //Retrieve user data from cookie
            HttpCookie user = Request.Cookies["usercookie"];
            string user_data = user.Value;
            Dictionary<string, object> user_vals = JsonConvert.DeserializeObject<Dictionary<string, object>>(user_data);

            int userId = Convert.ToInt32(user_vals["userId"]);
            string user_name = user_vals["username"].ToString();
            bool new_user = Convert.ToBoolean(user_vals["IsNew"]);  

            using (MyDbContext db = new MyDbContext())
            {
                string genres = form.v4;
                List<string> genre_list = new List<string>();
                if (genres != null)
                {
                    string[] items = genres.Split(',');

                    foreach (string i in items)
                    {
                        genre_list.Add(i);
                    }
                }
                if (ModelState.IsValid & genre_list.Count == 3)
                {
                    //Declare user features for encoding
                    string username = User.Identity.Name;
                    string experience = form.v1;
                    string gender = form.v2;
                    string generation = form.v3;
                    string fav_anime_period = form.v5;
                    var fav_genres = form.v4;

                    //string vector_values = v1+v2+

                    //changing the user IsNew value to false
                    var currentuser = db.userAccount.Find(userId);
                    currentuser.IsNew = false;
                    db.SaveChanges();
                    ModelState.Clear();

                    //Run k-neighbours
                    string file = @"C:\Final Project\anime-app\new_user.py";
                    string py = @"C:\Users\\titot\AppData\Local\Programs\Python\Python311\python.exe";
                    Process proc = new Process();
                    proc.StartInfo = new ProcessStartInfo(py, file)
                    {
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true,
                        Arguments = $"new_user.py new_user {experience}"
                    };
                    proc.Start();
                    string output = proc.StandardOutput.ReadToEnd();
                    proc.WaitForExit();
                    

                    return RedirectToAction("Dashboard", "UserAccount", new { new_user = false });
                }
                else
                {
                    //User didnt fill out all fields. Take them back to the dashboard to try again.
                    ViewBag.Welcome1 = "Please make sure you fill out all fields";
                    ViewBag.Welcome2 = "";
                    //return RedirectToAction("Dashboard","Home");
                    return View();
                }
            }
        }


    }
}