﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace anime_site.Models
{
    public class UserDetails
    {
        [Key]
        public int userId { get; set; }

        [Required(ErrorMessage ="Please enter a username")]
        public string username { get; set; }

        [Required(ErrorMessage = "Please enter a password")]
        public string password { get; set; }

 
        [NotMapped]
        public string ConfirmPassword { get; set; }


    }
}