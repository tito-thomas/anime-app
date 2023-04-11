using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace anime_site.Models
{
    public class NewQuestions
    {
        [Required(ErrorMessage ="Please fill out all fields")]
        public string v1 { get; set; }

        [Required(ErrorMessage = "Please fill out all fields")]
        public string v2 { get; set; }
        [Required(ErrorMessage = "Please fill out all fields")]
        public string v3 { get; set; }

        [Required(ErrorMessage = "Please fill out all fields")]
        public string v4{ get; set; }

        [Required(ErrorMessage = "Please fill out all fields")]
        public string v5 { get; set; }

    }
}
