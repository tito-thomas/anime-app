﻿using anime_site.Models;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Security.Cryptography.Xml;
using System.Web;
using System.Web.Mvc;

namespace anime_site.Controllers
{
    public class HomeController : Controller
    {

        public ActionResult Index()
        {

            if (User.Identity.IsAuthenticated){
                //if user is new:

                return RedirectToAction("Dashboard", "Home");
                //if user is not new:
                //go to dashboard
            }
            return View();               
        }

        public ActionResult Dashboard()
        {

            //Retrieve user data from cookie
            HttpCookie user = Request.Cookies["usercookie"];
            if (user != null) { 
            
                string user_data = user.Value;
                Dictionary<string, object> user_vals = JsonConvert.DeserializeObject<Dictionary<string, object>>(user_data);

                int userId = Convert.ToInt32(user_vals["userId"]);
                string user_name = user_vals["username"].ToString();
                bool new_user = Convert.ToBoolean(user_vals["IsNew"]);


                //Retrieve user preferences from database
                using (MyDbContext db = new MyDbContext())
                {
                    var currentuser = db.userAccount.Find(userId);
                    string p = currentuser.preferences;
                    string f = currentuser.fav_genres;
                    var recs = GetRecommendations(p, f);
                    ViewBag.Recs = recs;
                    return View();
                }
            }
            return RedirectToAction("Logout","UserAccount");
        }

        public object GetRecommendations(string preferences, string favgenres)
        {
            //Run python script to create user vector and then run k-neighbours
            string file = @"C:\Final Project\anime-app\new_user.py";
            string py = @"C:\Users\\titot\AppData\Local\Programs\Python\Python311\python.exe";
            //Process proc = new Process();
            ProcessStartInfo p = new ProcessStartInfo();
            p.FileName = py;
            p.Arguments = $"\"{file}\" \"{preferences}\" \"{favgenres}";
            p.UseShellExecute = false;
            p.CreateNoWindow = true;
            p.RedirectStandardOutput = true;
            p.RedirectStandardError = true;
            var e = "";
            var r = "";
            using (var proc = Process.Start(p))
            {
                e = proc.StandardError.ReadToEnd();
                r = proc.StandardOutput.ReadToEnd();
            }
            return r;
        }
    }
}