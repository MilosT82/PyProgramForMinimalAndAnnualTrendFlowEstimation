% Ulazna velicina je Q
n=length(Q);
r=autocorr(Q,1);
r1=r(2);


for i=1:n-1
    for j=i+1:n
  
        S(i,j)=sign(Q(i)-Q(j));
    end
end

Q1 = sort(Q,'descend');
Qmin=0.01*mean(Q);% Ukoliko je rezlika proticaja manja od ove vrednosti
% smatra se da su dva proticaja ista

for i=2:n
   delta_Q(i)=Q1(i-1)-Q1(i); 
   if delta_Q(i)>Qmin
       m(i)=0;
   else
       m(i)=1;
   end
end



S1=sum(sum(S))% ovo je Kendell-ova statistika

var_S1=(n*(n-1)*(2*n+5))/18;
std_S1=sqrt(var_S1);

if S1>0
    Zs=(S1-1)/std_S1
else
    Zs=(S1+1)/std_S1
end

% korekcija varijanse usled korelisanosti

CF2=1+2*(1-1/n)*r1;
var_S1_kor=var_S1*CF2;
std_S1_kor=sqrt(var_S1_kor);

if S1>0
    Zs_kor=(S1-1)/std_S1_kor
else
    Zs_kor=(S1+1)/std_S1_kor
end


y=normrnd(0,1,100000,1);% formiranje slucajnih brojeva po Gausovom zakonu
% raspodele sa elementima niza x

[f1,yi] = ksdensity(y);% funkcija gustine raspodele serije x
[f_cum_n,y_cum_n] = ecdf(y);% kumulativna raspodela
% sa y_cum_n se ocitava Zs, a dobija vrednost f_cum_n

min=min(y_cum_n);
max=max(y_cum_n);

X=min:0.01:max;
X1=X';

Y_cum = interp1q(y_cum_n,f_cum_n,X1); 

Zs_abs=abs(Zs);
Fcum = spline(X1,Y_cum,Zs_abs); % kumulativna verovatnoca po Normalnoj raspodeli
% za Zs

p=2*(1-Fcum)

Zs_abs_kor=abs(Zs_kor);
Fcum_kor = spline(X1,Y_cum,Zs_abs_kor); % kumulativna verovatnoca po Normalnoj raspodeli
% za Zs

p_kor=2*(1-Fcum_kor)
% BITNA NAPOMENA:
% Ako je abs(Zs)>1.96 tada je trend znacajan na nivou poverenja 5%
% p predstavlja prag znacajnosti trenda


