using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace anime_site.Models
{
    public class NewQuestions
    {

        [NotMapped]
        [Required(ErrorMessage ="Please fill out all fields")]
        public string v1 { get; set; }

        [NotMapped]
        [Required(ErrorMessage = "Please fill out all fields")]
        public string v2 { get; set; }

        [NotMapped]
        [Required(ErrorMessage = "Please fill out all fields")]
        public string v3 { get; set; }

        [NotMapped]
        [Required(ErrorMessage = "Please fill out all fields")]
        public string v4{ get; set; }

        [NotMapped]
        [Required(ErrorMessage = "Please fill out all fields")]
        public string v5 { get; set; }
    }
}
