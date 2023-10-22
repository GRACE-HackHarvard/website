S(document).ready(function() {
    var planetarium = S.virtualsky({
            id: 'starmap',
            projection: 'stereo', 
			latitude: 34.4326, 
			longitude: -119.86286
    });
});

function coord2horizon(ra, dec){
	var ha, alt, az, sd, sl, cl;
	// compute hour angle in degrees
	ha = (Math.PI*this.times.LST/12) - ra;
	sd = Math.sin(dec);
	sl = Math.sin(this.latitude.rad);
	cl = Math.cos(this.latitude.rad);
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

function radec2xy(ra,dec){
	var coords = this.coord2horizon(ra, dec);
	// Only return coordinates above the horizon
	//if(coords[0] > 0){
		var pos = azel2xy(coords[1]-(this.az_off*this.d2r),coords[0],this.wide,this.tall);
		return {x:pos.x,y:pos.y,az:coords[1]*this.r2d,el:coords[0]*this.r2d};
	//}
	// return 0;
};