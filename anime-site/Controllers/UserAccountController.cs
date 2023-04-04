using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Policy;
using System.Web;
using System.Web.Mvc;
using anime_site.Models;


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
            if (ModelState.IsValid) { //check if the username already exists in the database
                using (MyDbContext db = new MyDbContext()) {
                    //If the username is taken, try again
                    if (db.userAccount.Any(i=>i.username == user.username)){
                        ViewBag.Notification = "This username is taken, please try again";
                        return View();
                    }
                    else
                    {
                       db.userAccount.Add(user);
                       db.SaveChanges();
                       ModelState.Clear();
                       ViewBag.Message = user.username + " Registered";
                    }                       
                }
            }
            
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
                using (MyDbContext db = new MyDbContext())
                {
                    var auth = db.userAccount.Where(i => i.username.Equals(user.username) && i.password.Equals(user.password)).FirstOrDefault();
                    //var auth = db.userAccount.Single(i => i.username == user.username && i.password == user.password);
                    if (auth != null)
                    {
                        Session["username"] = user.username;
                        return RedirectToAction("Dashboard","Home");
                    }                       
           
                    else
                    {
                        ViewBag.Message = "Incorrect username or password";
                        return View();
                    }
                }
            }

        }

        public ActionResult Logout() 
        {

            Session.Clear();
            return View()
;        }

    }
}