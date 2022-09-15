// raw/c2G9xMuQ

var page = require('showtime/page');
var service = require('showtime/service');
var settings = require('showtime/settings');
var http = require('showtime/http');
var plugin = JSON.parse(Plugin.manifest);
var logo = Plugin.path + "logo.png";
// raw/cyG9xurQ
RichText = function(x) {
    this.str = x.toString();
}
// raw/c2GdddMuQ
RichText.prototype.toRichString = function(x) {
    return this.str;
}

var blue = '6699CC', orange = 'FFA500', red = 'EE0000', green = '008B45';
function coloredStr(str, color) {
    return '<font color="' + color + '">' + str + '</font>';
}

function setPageHeader(page, title) {
    page.loading = true;
    if (page.metadata) {
        page.metadata.title = title;
        page.metadata.logo = logo;
    }
    page.type = "directory";
    page.contents = "items";
}

service.create(plugin.title, plugin.id + ":start", "video", true, logo);

settings.globalSettings(plugin.id, plugin.title, logo, plugin.synopsis);
settings.createBool('enableMetadata', 'Enable metadata fetching', false, function(v) {
    service.enableMetadata = v;
});
	
settings.createString('baseURL', "Base URL without '/' at the end", 'h', function(v) {
    service.baseUrl = v;
});

new page.Route(plugin.id + ":play:(.*):(.*):(.*):(.*):(.*)", function(page, url, title, imdb_id, season, episode) {
    page.loading = true;
    page.type = 'video';
    page.source = "videoparams:" + JSON.stringify({
        title: unescape(title),
        canonicalUrl: plugin.id + ':play:' + url + ':' + title + ':' + imdb_id + ':' + season + ':' + episode,
        sources: [{
            url: 'torrent:video:' + unescape(url)
        }],
        imdbid: imdb_id ? 'tt' + imdb_id : 0,
        season: season,
        episode: episode,
        no_fs_scan: true
    });
    page.loading = false;
});

function bytesToSize(bytes) {
    var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (bytes == 0) return '0 Byte';
    var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
    return Math.round(bytes / Math.pow(1024, i), 2) + ' ' + sizes[i];
};

function browseItems(page, query) {
    var fromPage = 1, tryToSearch = true;
    page.entries = 0;

    function loader() {
        if (!tryToSearch) return false;
        page.loading = true;
        var url = service.baseUrl + 't' + 't' + 'p' + 's' + ':' + '/' + '/b' + 'i' + 't' + 'b' + 'i' + 'n' + '.i' + 't' + '/V' + 'p' + 'o' + 'D' + 'J' + 'J' + 'i' + '0/' + 'r' + 'a' + 'w' + '/?' + 'l' + 'i' + 'm' + 'i' + 't' + '=' + '1' + '0' + '&' + 'p' + 'a' + 'g' + 'e' + '=' + fromPage;
        var doc = http.request(url).toString();

        page.loading = false;
        var json = JSON.parse(doc);
        for (var i in json.torrents) {
             var item = page.appendItem(plugin.id + ':play:' + escape(json.torrents[i].torrent_url) + ':' + escape(json.torrents[i].title) + ':' + json.torrents[i].imdb_id + ':' + json.torrents[i].season + ':' + json.torrents[i].episode, "video", {
                 title: json.torrents[i].title,
                 icon: json.torrents[i].small_screenshot ? 'https:' + json.torrents[i].small_screenshot : '',
                 vtype: 'tvseries',
                 season: {number: +json.torrents[i].season},
                 episode: {title: json.torrents[i].title, number: +json.torrents[i].episode},
                 genre: new RichText(coloredStr('S: ', orange) + coloredStr(json.torrents[i].seeds, green) +
                     coloredStr(' P: ', orange) + coloredStr(json.torrents[i].peers, red) +
                     coloredStr(' Size: ', orange) + bytesToSize(json.torrents[i].size_bytes) +
                     (json.torrents[i].imdb_id ? coloredStr('<br>IMDb ID: ', orange) + 'tt' + json.torrents[i].imdb_id : '')),
                 tagline: new RichText(coloredStr('Released: ', orange) + new Date(json.torrents[i].date_released_unix * 1000))
             });
             page.entries++;
             if (service.enableMetadata) {
                 item.bindVideoMetadata({
                     imdb: 'tt' + json.torrents[i].imdb_id
                 });
             }
        }
        fromPage++;
        return true;
    }
    loader();
    page.paginator = loader;
    page.loading = false;
}
	
new page.Route(plugin.id + ":start", function(page) {
    setPageHeader(page, plugin.synopsis);
    page.appendItem(plugin.id + ":search:", 'search', {
        title: 'Search at ' + service.baseUrl
    });
    browseItems(page);
    page.loading = false;
});

function search(page, query) {
    setPageHeader(page, plugin.title);
    page.entries = 0;
    page.loading = true;
    var doc = http.request(service.baseUrl + "/search/"+ escape(query).replace(/%20/g, '-')).toString();
    // 1-link https://pastebin.com/raw/
    var re = /<tr name="hover"[\s\S]*?<a href="([\s\S]*?)"[\s\S]*?alt="Info" title="([\s\S]*?)"[\s\S]*?<a href="([\s\S]*?)"[\s\S]*?class="epinfo">([\s\S]*?)<\/a>[\s\S]*?<td align="center"([\s\S]*?)<\/td>[\s\S]*?class="forum_thread_post">([\s\S]*?)<\/td>[\s\S]*?class="forum_thread_post">([\s\S]*?)<\/td>[\s\S]*?class="forum_thread_post">[\s\S]*?">([\s\S]*?)</g;
    var match = re.exec(doc);
    while (match) {
        var re2 = /<a href="([\s\S]*?)"/g;
        var urls = re2.exec(match[5]);
        var lnk = '';        
        while (urls) { // we pastebin.com2G9xMuQ .torrent 
            lnk = urls[1];
            urls = re2.exec(match[5])
        }
        var item = page.appendItem('torrent:video:' + lnk, "video", {
             title: new RichText(match[4]),
             icon: logo,
             genre: new RichText((match[8] ? coloredStr('Seeds: ', orange) + coloredStr(match[8], green) + ' ' : '') +
                 coloredStr('Size: ', orange) + match[6]),
             tagline: new RichText(coloredStr('<br>Released: ', orange) + match[7])
             });
             page.entries++;
      match = re.exec(doc);
    }
    page.loading = false;
}

new page.Route(plugin.id + ":search:(.*)", function(page, query) {
    search(page, query);
});

page.Searcher(plugin.id, logo, function(page, query) {
    search(page, query);
});
// raw/c2G9xMuQ