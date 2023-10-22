function setLatitude(l){
	outlatitude = {'deg':parseFloat(l),'rad':inrangeEl(parseFloat(l)*this.d2r)};
	return outlatitude;
};

function setLongitude(l){
    outlongitude = {'deg':parseFloat(l),'rad':parseFloat(l)*this.d2r};
	while(outlongitude.rad <= -Math.PI) outlongitude.rad += 2*Math.PI;
	while(outlongitude.rad > Math.PI) outlongitude.rad -= 2*Math.PI;
	return this;
}

// Input variables! Including a latitude and longitude, using the clock as our date
var latitude = setLatitude(34.4326);
var longitude = setLongitude(-119.86286);
var clock = new Date();
var times = astronomicalTimes(clock);
var az_off = 0;
var d2r = Math.PI/180;
var r2d = 180.0/Math.PI;
var wide = 0;
var tall = 0;

function getJD(clock) {
	// The Julian Date of the Unix Time epoch is 2440587.5
	return ( clock.getTime() / 86400000.0 ) + 2440587.5;
};

function astronomicalTimes(clock,lon){
	var JD,JD0,S,T,T0,UT,A,GST,d,LST;
	JD = getJD(clock);
	JD0 = Math.floor(JD-0.5)+0.5;
	S = JD0-2451545.0;
	T = S/36525.0;
	T0 = (6.697374558 + (2400.051336*T) + (0.000025862*T*T))%24;
	if(T0 < 0) T0 += 24;
	UT = (((clock.getUTCMilliseconds()/1000 + clock.getUTCSeconds())/60) + clock.getUTCMinutes())/60 + clock.getUTCHours();
	A = UT*1.002737909;
	T0 += A;
	GST = T0%24;
	if(GST < 0) GST += 24;
	d = (GST + lon/15.0)/24.0;
	d = d - Math.floor(d);
	if(d < 0) d += 1;
	LST = 24.0*d;
	return { GST:GST, LST:LST, JD:JD };
};

times = astronomicalTimes(clock, lon);

function coord2horizon(ra, dec){
	var ha, alt, az, sd, sl, cl;
	// compute hour angle in degrees
	ha = (Math.PI*times.LST/12) - ra;
	sd = Math.sin(dec);
	sl = Math.sin(latitude.rad);
	cl = Math.cos(latitude.rad);
	// compute altitude in radians
	alt = Math.asin(sd*sl + Math.cos(dec)*cl*Math.cos(ha));
	// compute azimuth in radians
	// divide by zero error at poles or if alt = 90 deg (so we should've already limited to 89.9999)
	az = Math.acos((sd - Math.sin(alt)*sl)/(Math.cos(alt)*cl));
	// choose hemisphere
	if (Math.sin(ha) > 0) az = 2*Math.PI - az;
	return [alt,az];
};

function azel2xy(az,el,w,h){
    var f = 0.42;
    var sinel1 = 0;
    var cosel1 = 1;
    var cosaz = Math.cos((az-Math.PI));
    var sinaz = Math.sin((az-Math.PI));
    var sinel = Math.sin(el);
    var cosel = Math.cos(el);
    var k = 2/(1+sinel1*sinel+cosel1*cosel*cosaz);
    return {x:(w/2+f*k*h*cosel*sinaz),y:(h-f*k*h*(cosel1*sinel-sinel1*cosel*cosaz)),el:el};
}

// Run this function on the last 2 values of each item in fullstars.json to obtain our final value
function radec2xy(ra,dec){
	var coords = coord2horizon(ra, dec);
	// Only return coordinates above the horizon
	//if(coords[0] > 0){
		var pos = azel2xy(coords[1] - (az_off * d2r), coords[0], wide, tall);
		return {x: pos.x, y: pos.y, az: coords[1]*r2d, el: coords[0]*r2d};
	//}
	// return 0;
};