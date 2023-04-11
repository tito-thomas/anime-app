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

                return RedirectToAction("Dashboard", "UserAccount", new { new_user = false });
 
            }
            return View();               
        }

        //public ActionResult Dashboard(bool new_user=true)
        //{
            //if (new_user)
            //{
                //calculate user vector
            //}
        //    return View();
        //}
    }
}