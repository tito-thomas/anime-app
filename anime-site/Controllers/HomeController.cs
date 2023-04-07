using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace anime_site.Controllers
{
    public class HomeController : Controller
    {

        public ActionResult Index()
        {
            if (User.Identity.IsAuthenticated){

                return RedirectToAction("Dashboard", "Home");
 
            }
            return View();               
        }

        public ActionResult Dashboard()
        {

            return View();
        }
    }
}