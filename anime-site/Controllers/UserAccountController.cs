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
                                //Session["user_vector"] = user.user_vector;
                                FormsAuthentication.SetAuthCookie(user.username, true);
                                //If the user is new, pass argument that leads to first-time questions being asked
                                if (username_auth.IsNew)
                                {
                                   return RedirectToAction("Dashboard", "Home", new {new_user = true});
                                }
                                return RedirectToAction("Dashboard", "Home");
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

        public ActionResult ConstructVector()
        {


            return View();
        }

    }
}