
%64x64

close all;
clear;

%numOfFiles = 720;
total_images = 0;
groundTruth = [];
imageCounter = 1;
counter = 1;

for i=1:1051
    x = strcat('TrainData/output_', int2str(i-1), '.csv');;
    A = csvread(x); 
    %extract the lables of symbols
    dataValidation = size(find(A(:,1)>0),1);
    if(dataValidation > 2)
        noOfSymbols = size(find(A(2,:)>0),2);
        noOfStrokes = sum(A(1,1:noOfSymbols));
        groundTruth = horzcat(groundTruth, A(2,1:noOfSymbols));
        row_offset = 2;

        % size_of_row = size(A,2);

        for j=1:noOfSymbols  
            marktype={'none'};
            figure;
            set(gca,'xtick',[]);
            set(gca,'xticklabel',[]);
            set(gca,'ytick',[]);
            set(gca,'yticklabel',[]);
            set(gca, 'visible', 'off') ;
            
            hold on;
           
            for k=1:A(1,j)
                size_of_row = size(find(A(row_offset+k,:)>0),2);
                all_X = A(row_offset+k,1:2:size_of_row);
                all_Y = A(row_offset+k,2:2:size_of_row);   
                plot( all_Y, all_X);
            end
            
            img = getframe();
            
             
            imwrite(img.cdata, strcat('interm/tr',int2str(imageCounter),'.jpg'), 'quality', 95);
            
            img =  imread(strcat('interm/tr',int2str(imageCounter),'.jpg'));
            img = double(rgb2gray(img));
            img = imrotate(img,-90); 
            
            img = imresize(img,[64 64]);
            [gx gy] = gradient(img);
            g =  sqrt(gx.*gx + gy.*gy);
            img = g>5;
                
            se = strel('disk',1);
            imagelogical = imclose(img,se);
            imagelogical = ~imagelogical;
            all_symbols(imageCounter, 1, :,:) = imagelogical;
            all_symbols_backup(:,:,imageCounter) = imagelogical; 
            row_offset = row_offset+ A(1,j);
            imageCounter = imageCounter+1;
            hold off;
            close all
       end
       total_images = total_images+noOfSymbols;
       i
    end
   
end

%   for i=1:total_imagess
%      img =  imread(strcat('tr',int2str(i),'.jpg'));
%      img = double(rgb2gray(img));
%      img = imrotate(img,-90);
      
%      img = imresize(img,[50 50]);
%      [gx gy] = gradient(img);
%      g =  sqrt(gx.*gx + gy.*gy);
%      img = g>5;
      
%      imwrite(img, strcat('training\tr',int2str(i),'.jpg'));
%   end

