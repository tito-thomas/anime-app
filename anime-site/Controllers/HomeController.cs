using Newtonsoft.Json;
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
                //if user is new:

                return RedirectToAction("Welcome", "UserAccount");
                //if user is not new:
                //go to dashboard
            }
            return View();               
        }

        public ActionResult Dashboard()
        {

            //Retrieve user data from cookie
            HttpCookie user = Request.Cookies["usercookie"];
            string user_data = user.Value;
            Dictionary<string, object> user_vals = JsonConvert.DeserializeObject<Dictionary<string, object>>(user_data);

            int userId = Convert.ToInt32(user_vals["userId"]);
            string user_name = user_vals["username"].ToString();
            bool new_user = Convert.ToBoolean(user_vals["IsNew"]);

            return View();
            //if (new_user)
            //{
            //calculate user vector
            //}
            //    return View();
        }
    }
}