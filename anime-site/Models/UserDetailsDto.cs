using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace anime_site.Models
{
    public class UserDetailsDto
    {
        public int userId { get; set; }
        public string username { get; set; }
        public bool IsNew { get; set; }
    }
}
