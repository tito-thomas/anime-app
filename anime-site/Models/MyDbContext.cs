using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Data.Entity;

namespace anime_site.Models
{
    public class MyDbContext : DbContext
    {

        public MyDbContext() : base("name=Model1") { }
        public DbSet<UserDetails> userAccount { get; set; } 
    }
}