using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace anime_site.Models
{
    public class AnimeDetails
    {
        [Key]
        public int anime_id { get; set; }

        [Required]
        public string title { get; set; }

        [Required]
        public bool airing { get; set; }

        [Required]
        public int scored_by { get; set; }

        [Required]
        public int members { get; set; }

        [Required]
        public string studio { get; set; }

        [Required]
        public string genre{ get; set; }

        [Required]
        public int aired_from_year { get; set; }

        [Required]
        public string time_period { get; set; }

        [Required]
        public string fame { get; set; }

        public string image { get; set; }

    }
}